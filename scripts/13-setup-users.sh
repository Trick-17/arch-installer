#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

arch-chroot /mnt useradd -m -G wheel -s /bin/bash $USER_USERNAME
echo "Please type in a passwort for ${USER_USERNAME}:"
arch-chroot /mnt passwd $USER_USERNAME

### Place the user into the sudoers list
sed -i 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' /mnt/etc/sudoers