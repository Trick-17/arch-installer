#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt


echo " >> Choosing Timezone"
case $USER_TIMEZONE in
    "Deutschland") 
    arch-chroot /mnt ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime
    break;;

    "Schweiz") 
    arch-chroot /mnt ln -s /usr/share/zoneinfo/Europe/Zurich /etc/localtime
    break;;

* ) echo "Invalid input. Try again..."
        exit 1
esac

echo " >> Setting system clock"
arch-chroot /mnt hwclock --systohc --utc