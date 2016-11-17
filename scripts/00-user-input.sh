#!/bin/bash

###--------- Graphics -------------------------------
graphics=""  # Default graphics vendor
echo "Please choose your graphics vendor:"
select yn in "default" "intel" "nvidia" "amd" "vbox";
do
    case $yn in
        "default") 
        graphics="mesa mesa-libgl xf86-video-vesa opencl-mesa"
		break;;

        "intel") 
		graphics="mesa mesa-libgl xf86-video-intel opencl-mesa"
		break;;

        "nvidia") 
		graphics="nvidia nvidia-libgl opencl-nvidia"
		break;;

        "amd") 
        graphics="mesa mesa-libgl xf86-video-vesa opencl-mesa"
		break;;

        "vbox") 
        graphics="virtualbox-guest-modules-arch virtualbox-guest-utils opencl-mesa"
		break;;

	* ) echo "Invalid input. Try again..."
        exit 1
    esac
    break
done
###--------------------------------------------------


###--------- Packages -------------------------------
mindesktoppackages="yakuake"
fulldesktoppackages="chromium thunderbird texstudio gimp inkscape vlc teamspeak3 owncloud-client"
serverdesktoppackages=""

minpackages="base base-devel intel-ucode \
            sudo \
            wget \
            openssh \
            git \
            vim \
            zsh \
            powerline-fonts \
            archiso \
            p7zip \
            unrar \
            xclip \
            fortune-mod"
extrapackages="cmake \
                boost \
                eigen \
                ocl-icd \
                opencl-headers \
                openmpi \
                hdf5-cpp-fortran \
                python-pip \
                ipython \
                python-h5py \
                python-scipy \
                python-matplotlib \
                python-pillow \
                python-pylint \
                tree"
packages_selected=""
echo "Please choose your set of packages:"
select yn in "desktop full" "desktop minimal" "server";
do
    case $yn in
        "desktop full") 
        packages="$minpackages $extrapackages texlive-most texlive-lang doxygen graphviz filezilla qtox gnuplot"
        packages_selected=yn
		break;;

        "desktop minimal")
        packages="$minpackages"
        fulldesktoppackages=""
        packages_selected=yn
		break;;

        "server") 
		packages="$minpackages $extrapackages"
        packages_selected=yn
		break;;

	* ) echo "Invalid input. Try again..."
        exit 1
    esac
    break
done
###--------------------------------------------------


###--------- Desktop --------------------------------

echo "Please select the desktop you want to install"
select yn in "none" "kde plasma";
do 
    case $yn in
        "none")
        desktoppackages=""
        desktop_selected=yn
		break;;

        "kde plasma")
        desktoppackages="plasma sddm kde-applications $mindesktoppackages $fulldesktoppackages $serverdesktoppackages"
        desktop_selected=yn
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


###--------- Hostname -------------------------------
echo "Please type in a hostname (lowercase!):"
read -p 'Hostname: ' hostname
###--------------------------------------------------


###--------- Username -------------------------------
echo "Please type in a user name (lowercase!):"
read -p 'Username: ' username
###--------------------------------------------------


### Save the input in user-input.txt so we can read it back in later
echo "USER_GRAPHICS=\"$graphics\"" >> arch-installer/user-input.txt
echo "USER_PACKAGES=\"$packages\"" >> arch-installer/user-input.txt
echo "USER_PACKAGES_SELECTED=\"$packages_selected\"" >> arch-installer/user-input.txt
echo "USER_DESKTOP=\"$desktoppackages\"" >> arch-installer/user-input.txt
echo "USER_DESKTOP_SELECTED=\"$desktop_selected\"" >> arch-installer/user-input.txt
echo "USER_LANGUAGE=\"$language\"" >> arch-installer/user-input.txt
echo "USER_TIMEZONE=\"$timezone\"" >> arch-installer/user-input.txt
echo "USER_ZSH_THEME=\"$zshtheme\"" >> arch-installer/user-input.txt
echo "USER_HOSTNAME=\"$hostname\"" >> arch-installer/user-input.txt
echo "USER_USERNAME=\"$username\"" >> arch-installer/user-input.txt