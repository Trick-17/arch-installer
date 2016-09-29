### Install yaourt
# chmod +x arch-installer/yaourt.sh
# cp arch-installer/yaourt.sh /mnt/
# arch-chroot /mnt ./yaourt.sh

### Install aura
# chmod +x arch-installer/aura.sh
# cp arch-installer/aura.sh /mnt/
# arch-chroot /mnt ./aura.sh

### Install packages from AUR
# arch-chroot /mnt yaourt -S visual-studio-code --noconfirm
# arch-chroot /mnt aura -S visual-studio-code

echo " >> Going to install aur packages"
cp -r arch-installer/aur-packages/. /mnt/

arch-chroot /mnt sh createFakeUser.sh
arch-chroot /mnt su -u installer python installAurPackages.py
arch-chroot /mnt sh removeFakeUser.sh

rm /mnt/aurPackageList.txt /mnt/createFakeUser.sh /mnt/installAurPackages.py /mnt/removeFakeUser..sh
echo " >> Installed aur packages"