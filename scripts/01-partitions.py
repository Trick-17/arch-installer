import subprocess
from subprocess import run
from subprocess import check_output


print(" >> Fetching partitions from labels 'Arch' and 'EFI'")
try:
    device     = check_output("blkid -L Arch", shell=True, check=True).decode("utf-8")
    bootdevice = check_output("blkid -L EFI", shell=True, check=True).decode("utf-8")
except subprocess.CalledProcessError as error:
    print('Unable to figure out device and bootdevice...',
          ' Error message: ', error.output)


print(" >> Mounting 'Arch' partition on /mnt")
try:
    run("yes | mkfs.ext4 -L Arch "+device, shell=True)
    run("mount "+device+" /mnt", shell=True)
except subprocess.CalledProcessError as error:
    print("Unable to mount 'Arch' partition on /mnt...",
          ' Error message: ', error.output)


print(" >> Mounting 'EFI' boot partition on /mnt/boot")
try:
    run("mkdir -p /mnt/boot", shell=True)
    run("yes | mkfs.fat -F32 "+bootdevice, shell=True)
    run("fatlabel "+bootdevice+" EFI", shell=True)
    run("mount "+bootdevice+" /mnt/boot", shell=True)
except subprocess.CalledProcessError as error:
    print("Unable to mount 'EFI' partition on /mnt/boot...",
          ' Error message: ', error.output)
