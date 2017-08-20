cd /home/installer
pacman -S yajl expac --noconfirm
git clone https://aur.archlinux.org/cower.git
cd cower
makepkg
sudo pacman -U *.pkg.tar.xz --noconfirm
cd ..
git clone https://aur.archlinux.org/pacaur.git
cd pacaur
makepkg
sudo pacman -U *.pkg.tar.xz --noconfirm
cd ..