#!/bin/bash

###--------- Graphics -------------------------------
graphics=""  # Default graphics vendor
echo "Please choose your graphics vendor:"
select yn in "default" "intel" "nvidia" "amd" "vbox";
do
    case $yn in
        "default") 
        graphics="mesa mesa-libgl xf86-video-vesa"
		break;;

        "intel") 
		graphics="mesa mesa-libgl xf86-video-intel"
		break;;

        "nvidia") 
		graphics="nvidia nvidia-libgl"
		break;;

        "amd") 
        graphics="mesa mesa-libgl xf86-video-vesa"
		break;;

        "vbox") 
        graphics="virtualbox-guest-modules-arch virtualbox-guest-utils"
		break;;

	* ) echo "Invalid input. Try again..."
        exit 1
    esac
    break
done
###--------------------------------------------------


###--------- Graphics -------------------------------
echo "Please select the desktop you want to install"
select yn in "none" "kde plasma";
do 
    case $yn in
        "none")
        desktop="none"
		break;;

        "kde plasma") 
		desktop="plasma sddm kde-applications kdegraphics-okular chromium"
		break;;

	* ) echo "Invalid input. Try again..."
        exit 1
    esac
    break
done
###--------------------------------------------------


###--------- Languages ------------------------------
echo "Please choose your keyboard-layout and language:"
select language in "DE - Deutschland" "DE - Schweiz" "EN - DK" "EN - US";
do
    break
done
###--------------------------------------------------


###--------- Timezone -------------------------------
echo "Please choose your timezone:"
select timezone in "Deutschland" "Schweiz";
do
    break
done
###--------------------------------------------------


###--------- zsh Theme ------------------------------
echo "Please choose your zsh configuration:"
select zshtheme in "gideon" "nicholas" "josh" "sorin";
do
    break
done
###--------------------------------------------------


###--------- Hostname -------------------------------
echo "Please type in a hostname (lowercase!):"
read -p 'Hostname: ' hostname
###--------------------------------------------------


###--------- Username -------------------------------
echo "Please type in a user name (lowercase!):"
read -p 'Username: ' username
###--------------------------------------------------


echo "USER_GRAPHICS=\"$graphics\"" >> arch-installer/user-input.txt
echo "USER_DESKTOP=\"$desktop\"" >> arch-installer/user-input.txt
echo "USER_LANGUAGE=\"$language\"" >> arch-installer/user-input.txt
echo "USER_TIMEZONE=\"$timezone\"" >> arch-installer/user-input.txt
echo "USER_ZSH_THEME=\"$zshtheme\"" >> arch-installer/user-input.txt
echo "USER_HOSTNAME=\"$hostname\"" >> arch-installer/user-input.txt
echo "USER_USERNAME=\"$username\"" >> arch-installer/user-input.txt