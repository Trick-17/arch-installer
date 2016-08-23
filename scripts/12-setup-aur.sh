### Install yaourt
chmod +x arch-installer/yaourt.sh
cp arch-installer/yaourt.sh /mnt/
arch-chroot /mnt ./yaourt.sh

### Install packages from AUR
arch-chroot /mnt yaourt -S visual-studio-code --noconfirm