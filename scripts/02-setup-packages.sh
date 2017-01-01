#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

### Nicer formatting for pacstrap
sed -i 's/#Color/Color/g' /etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /etc/pacman.conf

### Update mirrorlist
reflector --verbose --latest 40 --sort rate --protocol https --save /etc/pacman.d/mirrorlist

### Setup Package List
echo " >> Creating package list"


#---------------------------------------------------------
#---------------------------------------------------------

packages_developer="cmake gnuplot boost eigen ocl-icd opencl-headers openmpi hdf5-cpp-fortran python-pip ipython python-h5py python-scipy python-matplotlib python-pillow python-pylint tree"
packages_full="$packages_developer texlive-most texlive-lang doxygen graphviz"

packages_desktop_developer_nogui=$packages_developer
packages_desktop_developer_gui="$packages_developer yakuake chromium"
packages_desktop_full_nogui=$packages_full
packages_desktop_full_gui="$packages_desktop_developer_gui texstudio filezilla qtox thunderbird  gimp inkscape vlc teamspeak3 owncloud-client"

packages_server_developer_nogui=$packages_developer
packages_server_developer_gui="$packages_developer yakuake chromium"
packages_server_full_nogui=$packages_full
packages_server_full_gui="$packages_server_developer_gui texstudio"


### System, Packages and Desktop
packages_user=""
case $USER_SYSTEM in
    "desktop") 
    case $USER_PACKAGES in
        "full") 
        case $USER_DESKTOP in
            "none") 
            packages_user=$packages_desktop_full_nogui
            ;;

            "kde plasma") 
            packages_user="plasma sddm kde-applications $packages_desktop_full_gui"
            ;;

        * ) echo "Invalid USER_DESKTOP. Try again..."
            exit 1
        esac
        ;;

        "developer") 
        case $USER_DESKTOP in
            "none") 
            packages_user=$packages_desktop_developer_nogui
            ;;

            "kde plasma") 
            packages_user="plasma sddm kde-applications $packages_desktop_developer_gui"
            ;;

        * ) echo "Invalid USER_DESKTOP. Try again..."
            exit 1
        esac
        ;;

        "minimal") 
        case $USER_DESKTOP in
            "none") 
            packages_user=""
            ;;

            "kde plasma") 
            packages_user="plasma sddm kde-applications"
            ;;

        * ) echo "Invalid USER_DESKTOP. Try again..."
            exit 1
        esac
        ;;

    * ) echo "Invalid USER_PACKAGES. Try again..."
        exit 1
    esac
    ;;

    "server") 
    case $USER_PACKAGES in
        "full") 
        case $USER_DESKTOP in
            "none") 
            packages_user=$packages_server_full_nogui
            ;;

            "kde plasma") 
            packages_user="plasma sddm kde-applications $packages_server_full_gui"
            ;;

        * ) echo "Invalid USER_DESKTOP. Try again..."
            exit 1
        esac
        ;;

        "developer") 
        case $USER_DESKTOP in
            "none") 
            packages_user=$packages_server_developer_nogui
            ;;

            "kde plasma") 
            packages_user="plasma sddm kde-applications $packages_server_developer_gui"
            ;;

        * ) echo "Invalid USER_DESKTOP. Try again..."
            exit 1
        esac
        ;;

        "minimal") 
        case $USER_DESKTOP in
            "none") 
            packages_user=""
            ;;

            "kde plasma") 
            user_packages="plasma sddm kde-applications"
            ;;

        * ) echo "Invalid USER_DESKTOP. Try again..."
            exit 1
        esac
        ;;

    * ) echo "Invalid USER_PACKAGES. Try again..."
        exit 1
    esac
    ;;

* ) echo "Invalid USER_SYSTEM. Try again..."
    exit 1
esac

### Graphics
packages_graphics=""
case $USER_GRAPHICS in
    "default") 
    packages_graphics="mesa mesa-libgl xf86-video-vesa opencl-mesa"
    ;;

    "intel") 
    packages_graphics="mesa mesa-libgl xf86-video-intel opencl-mesa"
    ;;

    "nvidia") 
    packages_graphics="nvidia nvidia-libgl opencl-nvidia"
    ;;

    "amd") 
    packages_graphics="mesa mesa-libgl xf86-video-vesa opencl-mesa"
    ;;

    "vbox") 
    packages_graphics="virtualbox-guest-modules-arch virtualbox-guest-utils opencl-mesa"
    ;;

* ) echo "Invalid USER_GRAPHICS. Try again..."
    exit 1
esac
#---------------------------------------------------------
#---------------------------------------------------------


### AUR packages dependencies
# yaourt needs yajl
# vs code needs gconf
# aura-bin needs abs
# AUR_DEPENDENCIES="gconf yajl abs"
# AUR_DEPENDENCIES="gconf abs"
AUR_DEPENDENCIES="abs"

### Install packages
echo " >> Going to install arch packages"
pacstrap /mnt base base-devel intel-ucode \
              sudo wget openssh git vim zsh powerline-fonts archiso p7zip unrar xclip fortune-mod reflector \
              $packages_user $packages_graphics abs
echo " >> Installed arch packages"

### Nicer formatting for pacstrap on installed
sed -i 's/#Color/Color/g' /mnt/etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /mnt/etc/pacman.conf


# Maybe later:
#   wpa_supplicant
#   nettle
