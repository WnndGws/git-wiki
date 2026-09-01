---
title: 0006-resize-arch-partitions
author: Wynand Gouws
date: 2026-09-01 08:26:57
public: true
---

1. [Step 1: Back up (boot into normal Arch system)](#step-1-back-up-boot-into-normal-arch-system)
2. [Step 2: Repartition (boot the live USB)](#step-2-repartition-boot-the-live-usb)
3. [Step 3: Encrypt both partitions](#step-3-encrypt-both-partitions)
4. [Step 4: Restore data](#step-4-restore-data)
5. [Step 5: Configure the system (chroot)](#step-5-configure-the-system-chroot)
6. [Step 6: Reboot](#step-6-reboot)
7. [References](#references)

## Step 1: Back up (boot into normal Arch system)

```Bash

# Mount external backup drive
mount /dev/sdY1 /mnt/backup

# Back up / (exclude pseudo-filesystems and the home mountpoint)
rsync -aAXv \
  --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/home/*"} \
  / /mnt/backup/root-backup/

# Back up /home
rsync -aAXv /home/ /mnt/backup/home-backup/

# Save config references
cp /etc/fstab /mnt/backup/fstab.orig
cp /etc/crypttab /mnt/backup/crypttab.orig
blkid > /mnt/backup/blkid.orig
lsblk -f > /mnt/backup/lsblk.orig

umount /mnt/backup
poweroff
```

## Step 2: Repartition (boot the live USB)

```Bash

# Confirm NVMe is nvme0n1.
lsblk

cfdisk /dev/nvme0n1
```

- Select nvme0n1p3 (the /home partition) -> Delete
- Select nvme0n1p2 (the / partition) -> Resize -> enter 100G
- Select the free space -> New -> press Enter to use all remaining (~137 GB)
- Write -> type yes -> Quit
- Verify using `lsblk`
  - should see nvme0n1p2 at 100 GB and nvme0n1p3 at ~137 GB, both with no mapper
    children.

## Step 3: Encrypt both partitions

```Bash

# Encrypt root
cryptsetup luksFormat /dev/nvme0n1p2

# Enter the same passphrase want to use for /home
cryptsetup open /dev/nvme0n1p2 cryptroot

# Create filesystem on root
mkfs.ext4 /dev/mapper/cryptroot

# Use mkfs.btrfs instead if that's what already had

# Encrypt home
cryptsetup luksFormat /dev/nvme0n1p3

# Enter the SAME passphrase as above
cryptsetup open /dev/nvme0n1p3 crypthome

# Create filesystem on home
mkfs.ext4 /dev/mapper/crypthome

# Use mkfs.btrfs instead if that's what already had
```

- The passphrases must be identical, this is what enables the keyring caching to
  work

## Step 4: Restore data

```Bash

# Mount backup drive
mount /dev/sdY1 /mnt/backup

# Mount new root
mount /dev/mapper/cryptroot /mnt

# Restore root
rsync -aAXv /mnt/backup/root-backup/ /mnt/

# Mount new home and restore
mkdir -p /mnt/home mount /dev/mapper/crypthome /mnt/home rsync -aAXv
/mnt/backup/home-backup/ /mnt/home/
```

## Step 5: Configure the system (chroot)

```Bash
mount /dev/nvme0n1p1 /mnt/boot arch-chroot /mnt

# Get the new UUIDs Bash
blkid

# Create /etc/crypttab.initramfs (root — unlocked in initramfs)
cat > /etc/crypttab.initramfs << 'EOF' cryptroot UUID=<UUID-of-nvme0n1p2> none
EOF

# Create /etc/crypttab (home — unlocked after boot, uses cached passphrase) Bash
cat > /etc/crypttab << 'EOF' crypthome UUID=<UUID-of-nvme0n1p3> none EOF

# Update /etc/fstab
cat > /etc/fstab << 'EOF'

# <device> <mount> <type> <options> <dump> <pass>
/dev/mapper/cryptroot / ext4 defaults 0 1 /dev/nvme0n1p1 /boot vfat defaults 0 2
/dev/mapper/crypthome /home ext4 defaults 0 2 tmpfs /tmp tmpfs nosuid,nodev 0 0
EOF

# Change ext4 to btrfs if that's what used.

# Update mkinitcpio hooks
vim /etc/mkinitcpio.conf

# Set the HOOKS line to Plaintext
HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block
sd-encrypt filesystems fsck)

# The sd-encrypt hook reads /etc/crypttab.initramfs and runs systemd-cryptsetup-generator in the initramfs.
# Update bootloader
ls /boot/loader/entries/

# Edit entry (e.g., /boot/loader/entries/arch.conf).
# Set the options line to:Plaintext
options root=/dev/mapper/cryptroot rw

# NB! Do not add any rd.luks.\* parameters — they conflict with crypttab.initramfs.

# Regenerate initramfs Bash
mkinitcpio -P
```

## Step 6: Reboot

```bash
# exit chroot
exit

umount -R /mnt cryptsetup close crypthome cryptsetup close cryptroot reboot

```

## References
