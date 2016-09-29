#!/bin/bash

arch-chroot /mnt userdel installer

sed -i '|installer ALL=(ALL) NOPASSWD: ALL|d' /mnt/etc/sudoers