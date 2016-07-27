Arch Installer
==============

This project aims to create an arch distro custom to the authors' needs.
It is based on archiso and takes inspiration from https://blog.chendry.org/automating-arch-linux-installation/,
where you may also find some descriptions to the various scripts etc.

This version will format your partitions and install Arch and download and install
a set of packages. It is not meant to keep bootloaders or disk formattings etc. intact!


Using this repository
=====================

Clone the repository and cd to *repo/releng*. Now execute

    sudo ./build.sh -v

An iso will be generated in the folder *repo/relelng/out*.
Booting a machine using this iso will land you in Arch's zsh-shell.
If *autorun.sh* executes on startup, you only need to answer the questions it asks.
Otherwise, call it yourself manually.

*autorun.sh* simply calls *install.sh*, which in turn calls the various installation scripts one after another.

**Note** that the installation requires a partition called *Arch*, since this procedure is primarily
intended for re-installation onto a pre-existing partition. You may thus have to `mkpart` beforehand.
Also note that for *autorun.sh* to run automatically you need EFI startup.

### A few necessary steps
In order for the *autorun.sh* script to work (specifically the *02-setup-partitions* script), you need to have
two partitions, named **EFI** and **Arch** respectively. If you are re-installing, and the partitions
already exist, you need not repeat this.

The developers used the following to prepare the disk:

    parted

    mklabel GPT
    mkpart ESP fat32 1MiB 513MiB
    set 1 boot on
    quit

    mkfs.ext4 -L Arch /dev/sda2
    mkfs.fat -F32 /dev/sda1
    fatlabel /dev/sda1 EFI

For more information see https://wiki.archlinux.org/index.php/GNU_Parted#UEFI.2FGPT_examples



Building your own repository
============================

Archiso
-------

Install archiso with

    sudo pacman -S archiso

You may start out with *baseline* or *releng*, this repository uses the latter.
To start with a clean new folder, copy it with

    cp /usr/share/archiso/configs/releng ~/arch-installer
    cd ~/arch-installer
    git init
    git commit -am "initial commit"

Running `build.sh` will fill the `work` and `out` folder, which is why they should be in your `.gitignore`.

As the installation scripts will require `git`, add it to the `packages.both` file.
Now run

    sudo ./build.sh -v

This will create an .iso in the /out subdirectory of the repo.
You may use dd to write this to a USB disk, e.g.:

    dd if=out/archlinux-2015.01.30-dual.iso of=/dev/sd_ bs=2M

**Booting from this image will land you in Arch's zsh-shell**.

Arch iso root filesystem
------------------------

The files in the folder *releng/airootfs* will be available to you in the root folder
when starting your live arch image.

autorun.sh
----------
Take a look at the /airootfs/root/.automated_script.sh file.
When the live system boots, the root user is automatically logged on, and this script is automatically executed.
The script looks at the options passed to the kernel (/proc/cmdline) and executes whatever is passed as the “script” parameter.

In */efiboot/loader/entries/archiso-x86_64-cd.conf*, you need to modify the last line:

    options archisobasedir=%INSTALL_DIR% archisolabel=%ARCHISO_LABEL% script=autorun.sh

Create a script *autorun.sh* in

    #!/bin/bash
    echo "hello, world"

Now, if you rebuild and boot from the ISO, it will automatically run the autorun.sh script and you’ll see “hello, world” output.

**Note**: you’ll need to clear out the /work directory before rebuilding.

Cloning and running the installation scripts
--------------------------------------------

Installation Scripts
--------------------