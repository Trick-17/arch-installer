#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

if [ "$USER_DESKTOP" != "none" ]
then
    arch-chroot /mnt sddm --example-config > /mnt/etc/sddm.conf

    sed -i 's/Current=maui/Current=breeze/g' /mnt/etc/sddm.conf
    sed -i 's/CursorTheme=/CursorTheme=breeze-dark/g' /mnt/etc/sddm.conf
    sed -i 's/Numlock=none/Numlock=on/g' /mnt/etc/sddm.conf

    arch-chroot /mnt systemctl enable sddm

    ### Copy desktop theme file s.t. all users automatically have this
    cp --parents arch-installer/configuration_desktop/* /mnt/etc/skel/
fi