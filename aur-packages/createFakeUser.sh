#!/bin/bash

arch-chroot /mnt useradd installer

echo "installer ALL=(ALL) NOPASSWD: ALL" >> /mnt/etc/sudoers