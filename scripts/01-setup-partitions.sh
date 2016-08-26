echo " >> Fetching devices from labels 'Arch' and 'EFI'"
device=$( blkid -L Arch )
bootdevice=$( blkid -L EFI )

echo " >> Mounting Arch partition on /mnt"
yes | mkfs.ext4 -L Arch $device
mount $device /mnt

echo " >> Mounting boot device on EFI partition"
mkdir -p /mnt/boot
yes | mkfs.fat -F32 $bootdevice 
fatlabel $bootdevice EFI
mount $bootdevice /mnt/boot