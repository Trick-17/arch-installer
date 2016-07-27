device=$( blkid -L Arch )
bootdevice=$( blkid -L EFI )

yes | mkfs.ext4 -L Arch $device
mount $device /mnt

mkdir -p /mnt/boot
yes | mkfs.fat -F32 $bootdevice 
fatlabel $bootdevice EFI

mount $bootdevice /mnt/boot