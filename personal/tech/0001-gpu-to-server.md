---
title: 0001-gpu-to-server
author: Wynand Gouws
date: 2026-04-12 14:37:39
public: true
---

# Adding GTX-1070 to Ubuntu server

* Ran the following commands after using ArchWiki to determine which drivers are needed

```bash
sudo add-apt-repository restricted multiverse
sudo apt update && sudo apt upgrade && sudo apt auto-remove
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo ubuntu-drivers list
sudo ubuntu-drivers install --gpgpu nvidia:580-server
```

* NB reboot!!!

# References

* freedesktop.org (2025). CodeNames.freedesktop.org. <https://nouveau.freedesktop.org/CodeNames.html#NV130>
* ArchWiki (2026). NVIDIA - ArchWiki. <https://wiki.archlinux.org/title/NVIDIA>
* UbuntuHandbook (2026). Ubuntu Added NVIDIA 580 Driver Support for 24.04, 22.04 26.04 UbuntuHandbook. <https://ubuntuhandbook.org/index.php/2025/09/ubuntu-added-nvidia-580-driver>
