# Detailed Arch Linux Setup Guide

## 1. Shell Configuration
### Change default shell to Nushell
```bash
# Install nushell
sudo pacman -S nushell

# Change shell for user wynand
sudo chsh -s "$(which nu)" wynand
```

## 2. Package Manager Setup
### Install and configure pikaur
```bash
# Install required dependencies
sudo pacman -S --needed base-devel git

# Clone and build pikaur
git clone https://aur.archlinux.org/pikaur.git
cd pikaur
makepkg -fsri
```

## 3. Security Configuration
### SSH Key Generation
```bash
# Install openssh
sudo pacman -S openssh

# Generate SSH key
ssh-keygen -t ed25519 -a 100 -C "your_email@example.com"
```

### GPG Configuration
```bash
# Import existing GPG key
gpg --import secret_key.asc

# Configure gpg-agent
cat > ~/.gnupg/gpg-agent.conf << EOL
enable-ssh-support
default-cache-ttl 60
max-cache-ttl 120
pinentry-program /usr/bin/pinentry-tty
EOL

# Set up GPG SSH socket
$env.SSH_AUTH_SOCK = (gpgconf --list-dirs agent-ssh-socket | str trim)

# Launch GPG agent
gpgconf --launch gpg-agent

# Add authentication subkey
gpg --expert --edit-key your@email.com
# In GPG shell:
# addkey
# Select option 8 (RSA - set your own capabilities)
# Toggle capabilities to authentication only (s,e,a,q)
# Select key size (4096)
# Set expiration

# Export keys
gpg --list-keys --with-subkey-fingerprints
gpg --export-ssh-key $KEY
```

## 4. Development Environment Setup
### Git Tools Installation
```bash
# Install git utilities
sudo pacman -S git-crypt
pikaur -S git-branchless
```

### Dotfiles Management
```bash
# Install stow
pikaur -S stow

# Clone dotfiles (after adding SSH key to GitHub)
git clone git@github.com:username/dotfiles.git

# Apply dotfiles
cd dotfiles
stow --restow --target="/home/wynand" ./*
```

## Key Configuration Files

### GPG Agent Configuration
Location: `~/.gnupg/gpg-agent.conf`
```conf
enable-ssh-support
default-cache-ttl 60
max-cache-ttl 120
pinentry-program /usr/bin/pinentry-tty
```

## Environment Variables
```nu
# GPG SSH Socket Configuration
$env.SSH_AUTH_SOCK = (gpgconf --list-dirs agent-ssh-socket | str trim)
```

## System Dependencies Overview
1. Base Development Tools:
   - base-devel
   - git

2. Security Tools:
   - openssh
   - gpg (usually pre-installed)

3. Development Tools:
   - git-crypt
   - git-branchless
   - stow

4. Shell:
   - nushell

## Post-Installation Verification Steps
1. Verify shell change:
   ```bash
   echo $SHELL
   ```

2. Verify GPG setup:
   ```bash
   gpg --list-keys
   gpg --list-secret-keys
   ```

3. Verify SSH agent:
   ```bash
   ssh-add -l
   ```

4. Verify dotfiles:
   ```bash
   ls -la ~/ | grep -e "^l"
   ```
