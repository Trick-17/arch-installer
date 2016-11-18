#!/bin/bash

###--------- System Type --------------------------
echo "Please choose your kind of system:"
select user_system in "desktop" "server";
do
    break
done
###--------------------------------------------------

###--------- Package Level --------------------------
echo "Please choose your set of packages:"
select user_packages in "full" "developer" "minimal";
do
    break
done
###--------------------------------------------------

###--------- Desktop --------------------------------
echo "Please choose your graphics drivers:"
select user_desktop in "none" "kde plasma";
do
    break
done
###--------------------------------------------------

###--------- Graphics Drivers -----------------------
echo "Please choose your graphics drivers:"
select user_graphics in "default" "intel" "nvidia" "amd" "vbox";
do
    break
done
###--------------------------------------------------


###--------- Languages ------------------------------
echo "Please choose your keyboard-layout and language:"
select user_language in "DE - Deutschland" "DE - Schweiz" "EN - DK" "EN - US";
do
    break
done
###--------------------------------------------------


###--------- Timezone -------------------------------
echo "Please choose your timezone:"
select user_timezone in "Deutschland" "Schweiz";
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


### Save the input in user-input.txt so we can read it back in later
echo "USER_SYSTEM=\"$user_system\""     >> arch-installer/user-input.txt
echo "USER_PACKAGES=\"$user_packages\"" >> arch-installer/user-input.txt
echo "USER_DESKTOP=\"$user_desktop\""   >> arch-installer/user-input.txt
echo "USER_GRAPHICS=\"$user_graphics\"" >> arch-installer/user-input.txt
echo "USER_LANGUAGE=\"$user_language\"" >> arch-installer/user-input.txt
echo "USER_TIMEZONE=\"$user_timezone\"" >> arch-installer/user-input.txt
echo "USER_HOSTNAME=\"$hostname\""      >> arch-installer/user-input.txt
echo "USER_USERNAME=\"$username\""      >> arch-installer/user-input.txt