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

# Create fake install user
arch-chroot /mnt useradd -m installer
echo "installer ALL=(ALL) NOPASSWD: ALL" >> /mnt/etc/sudoers

# Copy install files to fake install user home directory
cp arch-installer/aur-packages/aurPackageList.txt /mnt/home/installer/
cp arch-installer/aur-packages/installAurPackages.py /mnt/home/installer/

# Install aura and AUR packages 
arch-chroot /mnt sudo -u installer python /home/installer/installAurPackages.py

# Remove fake install user
arch-chroot /mnt userdel installer
sed -i '/installer ALL=(ALL) NOPASSWD: ALL/d' /mnt/etc/sudoers
rm -rf /mnt/home/installer

echo " >> Installed aur packages"