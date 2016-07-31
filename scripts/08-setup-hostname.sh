#!/bin/bash
echo "Please type in a hostname (lowercase!):"
read -p 'Hostname: ' varname
echo $varname > /mnt/etc/hostname

sed -i '/^127/ s/$/ $varname' /mnt/etc/hosts
sed -i '/^::1/ s/$/ $varname' /mnt/etc/hosts