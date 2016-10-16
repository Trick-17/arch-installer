#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

### Nicer formatting for pacstrap
sed -i 's/#Color/Color/g' /etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /etc/pacman.conf

### AUR packages dependencies
# yaourt needs yajl
# vs code needs gconf
# aura-bin needs abs
# AUR_DEPENDENCIES="gconf yajl abs"
# AUR_DEPENDENCIES="gconf abs"
AUR_DEPENDENCIES="abs"

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
    python-pip \
    ipython \
    powerline-fonts \
    archiso \
    yakuake \
    texlive-most texlive-lang \
    p7zip \
    unrar \
    boost \
    eigen \
    python-h5py \
    hdf5-cpp-fortran \
    doxygen \
    xclip \
    graphviz \
    tree \
    filezilla \
    ocl-icd \
    opencl-headers \
    $AUR_DEPENDENCIES \
    $USER_GRAPHICS $USER_DESKTOP
echo " >> Installed arch packages"

### Nicer formatting for pacstrap on installed
sed -i 's/#Color/Color/g' /mnt/etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /mnt/etc/pacman.conf


# Maybe later:
#   wpa_supplicant
#   nettle
