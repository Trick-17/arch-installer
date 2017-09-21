Arch Installer
==============

This project aims to provide you with a pure Arch-Linux experience but without the hassle of all the manual installation
steps one has to perform. Thus this project provides an installation script that performs common installation steps like
setting up the locale and installing commonly used packages.

All packages are installed via the package manager `pacman`.
Therefore, after installation you can modify everything to your liking as in a pure arch-linux installation.
Note that `pacaur` is built, installed and used to install further AUR packages.

The initial inspiration and the concept for this project were taken from this blog: https://blog.chendry.org/automating-arch-linux-installation/. This blog also contains useful information how to create 
a custom installer medium.
Most of the inital installation steps are quite universal and were taken from the [Arch Beginners Guide](https://wiki.archlinux.org/index.php/Beginners%27_guide) from which the
developers took helpful information and guidance. It is always
a useful source, especially if you want to fork this project to modify it to your needs.

This version will format your partitions and install Arch and download and install
a set of packages and terminal/desktop styles. It is not meant to keep bootloaders or disk formattings etc. intact!


Using this repository
=====================

You may simply download an iso from the [latest release](https://github.com/Trick-17/arch-installer/releases) and prepare a bootable medium with it.
If you do not have the partitions set up look into the section [Pre-installation partitioning](#Partitions).

Booting a machine using this iso will land you in Arch's zsh-shell.
You may use `./autorun.sh` to start the installation process. You will be asked a series of questions, after which corresponding settings are made and packages downloaded and installed.

> Note that the default keyboard layout is US so in case you have a different keyboard layout you have to look up the mapping for the `./`. You can then choose your keyboard layout during installation before anything needs to be typed.

## Pre-installation partitioning  <a name="Partitions"></a>
The installation requires two partitions, called `Arch` and `EFI` respectively, since this procedure is primarily
intended for re-installation onto a pre-existing partition. You may thus have to `mkpart` beforehand.
If you want to avoid overriding your partitions you have to modify the `01_partitions` script in
the `pyscripts` folder.

The following or variations of it can be used to prepare the disk:

    parted

    mklabel GPT
    mkpart ESP fat32 1MiB 513MiB
    mkpart primary ext4 513MiB 100%
    set 1 boot on
    quit

    mkfs.ext4 -L Arch /dev/sda2
    mkfs.fat -F32 /dev/sda1
    fatlabel /dev/sda1 EFI

Alternatively you can manually call `./prepare_disk.sh`.
For more information see [wiki.archlinux.org](https://wiki.archlinux.org/index.php/GNU_Parted#UEFI.2FGPT_examples).

## VirtualBox
If you are using VirtualBox, be aware of the following:
- EFI needs to be activated (Settings -> System) 
- nested paging needs to be deactivated (Settings -> System -> Processor).


Building your own installer ISO
===============================

Using `archiso`, you can generate your own iso to boot into. To do this, switch to a folder of your choice and execute the following commands:

    sudo pacman -S archiso
    git clone https://github.com/Trick-17/arch-installer.git
    cd arch-installer/releng
    sh createIso.sh

An iso will be generated in the sub-folder `out`.
Note that you can of course modify certain files in order to e.g. add further packages to the live iso (see also https://blog.chendry.org/automating-arch-linux-installation/).