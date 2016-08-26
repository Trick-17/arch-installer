#!/bin/bash

# Go to /tmp
cd /tmp
rm -rf install-aura # Make sure the install-aura folder doesn't exist
mkdir install-aura # Create working dir
cd install-aura # Switch to the working dir

# Download archives (from AUR)
wget https://aur.archlinux.org/cgit/aur.git/snapshot/aura.tar.gz # aura snapshot

# Exctract archives
tar -xzvf aura.tar.gz

# Write permissions
chgrp nobody aura
chmod g+ws aura
setfacl -m u::rwx,g::rwx aura
setfacl -d --set u::rwx,g::rwx,o::- aura

# Install packages
cd aura
sudo -u nobody makepkg -s # Creates the package
sudo pacman -U aura*.pkg.tar.xz --noconfirm # Installs the package
cd ..