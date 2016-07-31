#!/bin/bash
echo "Please choose your timezone:"
select yn in "Deutschland" "Schweiz";
do 
    case $yn in
        "Deutschland") 
		arch-chroot /mnt ln -s /usr/share/zoneinfor/Europe/Berlin
        break;;

        "Schweiz") 
		arch-chroot /mnt ln -s /usr/share/zoneinfor/Europe/Zurich
        break;;

	* ) echo "Invalid input. Try again..."
            exit 1
    esac
    break
done

arch-chroot /mnt nwclock --systohc --utc