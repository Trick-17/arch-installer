#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

echo $USER_HOSTNAME > /mnt/etc/hostname

sed -i "/^127/ s/$/ ${USER_HOSTNAME}/" /mnt/etc/hosts
sed -i "/^::1/ s/$/ ${USER_HOSTNAME}/" /mnt/etc/hosts