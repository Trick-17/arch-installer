#!/bin/bash
echo "Please choose your keyboard-layout and language:"
select yn in "DE - Deutschland" "DE - Schweiz" "EN - DK" "EN - US";
do 
    case $yn in
        "DE - Deutschland") 
		loadkeys de-latin1
		arch-chroot /mnt localectl set-keymap de-latin1
		sed -i 's/#en_DK.UTF-8/en_DK.UTF-8/g' /mnt/etc/locale.gen
		echo LANG=en_DK.UTF-8 > arch-installer/locale.conf
		break;;

        "DE - Schweiz") 
		loadkeys sg-latin1
		arch-chroot /mnt localectl set-keymap sg-latin1
		sed -i 's/#en_DK.UTF-8/en_DK.UTF-8/g' /mnt/etc/locale.gen
		echo LANG=en_DK.UTF-8 > arch-installer/locale.conf
		break;;

        "EN - DK")
		arch-chroot /mnt localectl set-keymap us
		sed -i 's/#en_DK.UTF-8/en_DK.UTF-8/g' /mnt/etc/locale.gen
		echo LANG=en_DK.UTF-8 > arch-installer/locale.conf
		break;;

		"EN - US")
		arch-chroot /mnt localectl set-keymap us
		sed -i 's/#en_US.UTF-8/en_US.UTF-8/g' /mnt/etc/locale.gen
		echo LANG=en_US.UTF-8 > arch-installer/locale.conf
		break;;
	* ) echo "Invalid input. Try again..."
            exit 1
    esac
    break
done


cp arch-installer/locale.conf /mnt/etc/


arch-chroot /mnt locale-gen