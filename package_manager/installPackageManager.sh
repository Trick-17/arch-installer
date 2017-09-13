gpg --recv-keys --keyserver hkp://pgp.mit.edu 1EB2638FF56C0C53
cd /home/installer
sudo pacman -S yajl expac --noconfirm
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