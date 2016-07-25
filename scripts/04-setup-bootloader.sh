mkdir -p /mnt/boot
mount $( blkid -L EFI ) /mnt/boot

bootctl --path=/mnt/boot install

cat <<-END > /mnt/boot/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options root=PARTUUID=$( blkid -s PARTUUID -o value $( blkid -L Arch ) )
END

cat <<-END > /mnt/boot/loader/loader.conf
default arch
timeout 4
editor  0
END