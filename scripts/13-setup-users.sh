#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

arch-chroot /mnt useradd -m -G wheel -s /bin/bash $USER_USERNAME
echo "Please type in a password for ${USER_USERNAME}:"
arch-chroot /mnt passwd $USER_USERNAME

echo "Please type in a password for root user:"
arch-chroot /mnt passwd

### Place the user into the sudoers list
sed -i 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' /mnt/etc/sudoers
