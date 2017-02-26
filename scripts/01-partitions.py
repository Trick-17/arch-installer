import subprocess
from utilities import run
from utilities import check_output

def create_and_mount():
    print(" >> Fetching partitions from labels 'Arch' and 'EFI'")
    try:
        device     = check_output("blkid -L Arch")
        bootdevice = check_output("blkid -L EFI")
    except subprocess.CalledProcessError as error:
        print('Unable to figure out linux and boot partition. You need to label the linux partition `Arch`'
            ' and the boot partition `EFI` for auto-detection to work.',
            ' Error message: ', error.output)


    print(" >> Mounting 'Arch' partition on /mnt")
    try:
        run("yes | mkfs.ext4 -L Arch "+device)
        run("mount "+device+" /mnt")
    except subprocess.CalledProcessError as error:
        print("Unable to mount 'Arch' partition on /mnt .",
            ' Error message: ', error.output)


    print(" >> Mounting 'EFI' boot partition on /mnt/boot")
    try:
        run("mkdir -p /mnt/boot")
        run("yes | mkfs.fat -F32 "+bootdevice)
        run("fatlabel "+bootdevice+" EFI")
        run("mount "+bootdevice+" /mnt/boot")
    except subprocess.CalledProcessError as error:
        print("Unable to mount 'EFI' partition on /mnt/boot .",
            ' Error message: ', error.output)
