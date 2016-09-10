#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

if [ "$USER_DESKTOP" != "none" ]
then
    echo " >> Activating Desktop (sddm)"

    arch-chroot /mnt sddm --example-config > /mnt/etc/sddm.conf

    sed -i 's/Current=maui/Current=breeze/g' /mnt/etc/sddm.conf
    sed -i 's/CursorTheme=/CursorTheme=breeze-dark/g' /mnt/etc/sddm.conf
    sed -i 's/Numlock=none/Numlock=on/g' /mnt/etc/sddm.conf

    arch-chroot /mnt systemctl enable sddm

    ### Copy desktop theme file s.t. all users automatically have this
    echo " >> Copying Desktop and Shell theme files"
    mkdir -p /mnt/etc/skel/.config/
    mkdir -p /mnt/etc/skel/.local/share/konsole/
    cp arch-installer/configuration_desktop/.config/kdeglobals /mnt/etc/skel/.config/
    cp arch-installer/configuration_desktop/.config/konsolerc /mnt/etc/skel/.config/
    cp arch-installer/configuration_desktop/.config/yakuakerc /mnt/etc/skel/.config/
    cp arch-installer/configuration_desktop/.config/kcminputrc /mnt/etc/skel/.config/
    cp arch-installer/configuration_desktop/.local/share/konsole/Default.profile /mnt/etc/skel/.local/share/konsole/
    cp arch-installer/configuration_desktop/.local/share/konsole/Dark\ Breeze.colorscheme /mnt/etc/skel/.local/share/konsole/
    cp arch-installer/configuration_desktop/.gtkrc-2.0 /mnt/etc/skel/
fi