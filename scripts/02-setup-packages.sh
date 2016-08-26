#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

### Nicer formatting for pacstrap
sed -i 's/#Color/Color/g' /etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /etc/pacman.conf

### Install packages
pacstrap /mnt base base-devel intel-ucode \
    sudo \
    wget \
    openssh \
    git \
    cmake \
    vim \
    zsh \
    powerline-fonts \
    archiso \
    yakuake \
    $USER_GRAPHICS $USER_DESKTOP

### Nicer formatting for pacstrap on installed
sed -i 's/#Color/Color/g' /mnt/etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /mnt/etc/pacman.conf

# pacstrap -c /mnt \
#   base base-devel intel-ucode \             # Always necessary! base-devel includes gcc
#   openssh \                     # Open SSH client
#   wget \                        # Download stuff from the web in your shell
#   vim \                         # Editor
#   ttf-dejavu \                  # Nice font
#   adobe-source-code-pro-fonts \ # Nice Adobe font
#   git \
#   python \
#   cmake \
#   archiso \
#   $USER_GRAPHICS \                   # Graphics (determined by vendor)
#   plasma \                      # KDE Desktop group
#   sddm \                        # Window manager
#   kde-applications \            # Useful desktop apps
#   kdegraphics-okular \          # PDF reader
#   firefox \
#   zsh \

# later
#   vscode \

# maybe
#   wpa_supplicant \
#   nettle \
