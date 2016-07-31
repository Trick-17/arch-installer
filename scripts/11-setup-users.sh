echo "Please type in a user name (lowercase!):"
read -p 'Username: ' username

arch-chroot /mnt useradd -m -G wheel -s /bin/bash $username
echo "Please type in a passwort for ${username}:"
arch-chroot /mnt passwd $username

### Place the user into the sudoers list
sed -i 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' /mnt/etc/sudoers