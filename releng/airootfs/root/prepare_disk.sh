### Generate GPT label, create fat32 partition ESP, create ext4 partition primary
parted /dev/sda mklabel GPT mkpart ESP fat32 1MiB 513MiB mkpart primary ext4 513MiB 100% set 1 boot on
### Create ext4 filesystem as /dev/sda2
mkfs.ext4 -L Arch /dev/sda2
### Create fat32 filesystem as /dev/sda1
mkfs.fat -F32 /dev/sda1
### Create fat-label EFI for /dev/sda1
fatlabel /dev/sda1 EFI