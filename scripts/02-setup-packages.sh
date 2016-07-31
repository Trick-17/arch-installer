#!/bin/bash
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

desktop=""
echo "Please select the desktop you want to install"
select yn in "none" "kde plasma";
do 
    case $yn in
        "none")
		break;;

        "kde plasma") 
		desktop="plasma sddm kde-applications kdegraphics-okular firefox"
		break;;

	* ) echo "Invalid input. Try again..."
            exit 1
    esac
    break
done


### nicer formatting for pacstrap
sed -i 's/#Color/Color/g' /etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /etc/pacman.conf

### install packages
pacstrap /mnt base base-devel intel-ucode \
    sudo \
    wget \
    openssh \
    git \
    vim \
    zsh \
    $graphics $desktop

### nicer formatting for pacstrap on installed
sed -i 's/#Color/Color/g' /mnt/etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /mnt/etc/pacman.conf

# pacstrap -c /mnt \
#   base base-devel intel-ucode \             # Always necessary! base-devel includes gcc
#   openssh \                     # Open SSH client
#   wget \                        # Download stuff from the web in your shell
#   vim \                         # Editor
#   ttf-dejavu \                  # Nice font
#   adobe-source-code-pro-fonts \ # Nice Adobe font
#   git \
#   python \
#   cmake \
#   archiso \
#   $graphics \                   # Graphics (determined by vendor)
#   plasma \                      # KDE Desktop group
#   sddm \                        # Window manager
#   kde-applications \            # Useful desktop apps
#   kdegraphics-okular \          # PDF reader
#   firefox \
#   zsh \

# later
#   vscode \

# maybe
#   wpa_supplicant \
#   nettle \