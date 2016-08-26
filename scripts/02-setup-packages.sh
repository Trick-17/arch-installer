#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

### Nicer formatting for pacstrap
sed -i 's/#Color/Color/g' /etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /etc/pacman.conf

### AUR packages dependencies
# yaourt needs yajl
# vs code needs gconf
AUR_DEPENDENCIES="gconf yajl"

### Install packages
echo " >> Going to install arch packages"
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
    thunderbird \
    texstudio \
    texlive-most texlive-lang \
    vlc \
    $AUR_DEPENDENCIES \
    $USER_GRAPHICS $USER_DESKTOP
echo " >> Installed arch packages"

### Nicer formatting for pacstrap on installed
sed -i 's/#Color/Color/g' /mnt/etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /mnt/etc/pacman.conf


# Maybe later:
#   wpa_supplicant
#   nettle
