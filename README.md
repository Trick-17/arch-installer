Arch Installer
==============

This project aims to provide you with a pure Arch-Linux experience but without the hassle of all the manual installation
steps one has to perform. Thus this project provides an installation script that performs common installation steps like
setting up the locale and installing commonly used packages. All packages are installed via the package manager pacman.
Therefore, after installation you can modify everything to your liking as in a pure arch-linux installation.

The initial inspiration and the concept for this project were taken from this blog: https://blog.chendry.org/automating-arch-linux-installation/. This blog also contains useful information how to create 
a custom installer medium.

This version will format your partitions and install Arch and download and install
a set of packages and terminal/desktop styles. It is not meant to keep bootloaders or disk formattings etc. intact!

Most of the inital installation steps are quite universal and were taken from the Arch Beginners Guide from which the
developers took helpful information and guidance: https://wiki.archlinux.org/index.php/Beginners%27_guide. It is always
a useful source, especially if you want to fork this project to modify it to your needs.


Using this repository
=====================

## Using archiso
Switch to a folder of your choice and execute the following commands:

    sudo pacman -S archiso
    git clone https://github.com/GPMueller/arch-installer.git
    cp -r /usr/share/archiso/configs/releng ~/arch-installer-iso
    cp -rf arch-installer/releng arch-installer-iso
Then to build switch into the folder and call the build script:

    cd arch-installer-iso
    sudo ./build.sh -v

(see also https://blog.chendry.org/automating-arch-linux-installation/).
Note you may also use the folder `baseline` instead of `releng`.
An iso will be generated in the folder `repo/relelng/out`.

Booting a machine using this iso will land you in Arch's zsh-shell.
If you do not have the partitions set up look into the section [Partitions](#Partitions).
Otherwise call `./autorun.sh` to install Arch.
> Note that the keyboard layout is US so in case you have a different keyboard layout you have to look up the mapping for the `./`.


## Partitions  <a name="Partitions"></a>
The installation requires a partition called *Arch*, since this procedure is primarily
intended for re-installation onto a pre-existing partition. You may thus have to `mkpart` beforehand.
Also note that an `EFI` partition is required.
If you want to avoid overriding your partitions you have to modify the `02-setup-partitions` script in
the scripts folder.

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
For more information see https://wiki.archlinux.org/index.php/GNU_Parted#UEFI.2FGPT_examples


## VirtualBox
If you are using VirtualBox, be aware.
> - EFI needs to be activated (Settings -> System) 
> - nested paging needs to be deactivated (Settings -> System -> Processor).
