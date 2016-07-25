#!/bin/bash
graphics = "mesa mesa-libgl xf86-video-wesa"  # Default graphics vendor
echo "Please choose your graphics vendor:"
select yn in "default" "intel" "nvidia" "amd";
do 
    case $yn in
        "default")
		break;;

        "intel") 
		graphics = "mesa mesa-libgl xf86-video-intel"
		break;;

        "nvidia") 
		graphics = "nvidia nvidia-libgl"
		break;;

        "amd") 
		# graphics = "mesa mesa-libgl"
		break;;

	* ) echo "Invalid input. Try again..."
            exit 1
    esac
    break
done

# nicer formatting for pacstrap
sed -i 's/#Color/Color/g' /etc/pacman.conf
sed -i 's/#TotalDownload/TotalDownload/g' /etc/pacman.conf

# install packages
pacstrap -c /mnt \
  base base-devel \
  openssh \
  wget \
  vim \
  ttf-dejavu \
  adobe-source-code-pro-fonts \
  git \
  python \
  cmake \
  archiso \
  $graphics \
  plasma \
  sddm \
  kde-applications \
  kdegraphics-okular \
  firefox \
  zsh

# pacstrap -c /mnt \
#   base base-devel \             # Always necessary! base-devel includes gcc
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
#   zsh

# later
#   vscode \

# maybe
#   wpa_supplicant \
#   nettle \