#!/bin/bash
echo "Please choose your timezone:"
select yn in "Deutschland" "Schweiz";
do 
    case $yn in
        "Deutschland") 
		arch-chroot /mnt ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime
        break;;

        "Schweiz") 
		arch-chroot /mnt ln -s /usr/share/zoneinfo/Europe/Zurich /etc/localtime
        break;;

	* ) echo "Invalid input. Try again..."
            exit 1
    esac
    break
done

arch-chroot /mnt hwclock --systohc --utc