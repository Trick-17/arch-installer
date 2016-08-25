#!/bin/bash

# Go to /tmp
cd /tmp
rm -rf install-yaourt # Make sure the install-yaourt folder doesn't exist
mkdir install-yaourt # Create working dir
cd install-yaourt # Switch to the working dir

# Download archives (from AUR)
wget https://aur.archlinux.org/cgit/aur.git/snapshot/package-query.tar.gz # package-query snapshot
wget https://aur.archlinux.org/cgit/aur.git/snapshot/yaourt.tar.gz # yaourt snapshot

# Exctract archives
tar -xzvf package-query.tar.gz
tar -xzvf yaourt.tar.gz

# Write permissions
chgrp nobody package-query
chmod g+ws package-query
setfacl -m u::rwx,g::rwx package-query
setfacl -d --set u::rwx,g::rwx,o::- package-query
chgrp nobody yaourt
chmod g+ws yaourt
setfacl -m u::rwx,g::rwx yaourt
setfacl -d --set u::rwx,g::rwx,o::- yaourt

# Install packages
cd package-query
sudo -u nobody makepkg # Creates the package
sudo pacman -U package-query*.pkg.tar.xz --noconfirm # Installs the package
cd ..

cd yaourt
sudo -u nobody makepkg # Creates the package
sudo pacman -U yaourt*.pkg.tar.xz --noconfirm # Installs the package
cd ..