import subprocess
from pyscripts.utilities import run
from pyscripts.utilities import check_output


def configure_bootloader():
    # Call to generate most default files and folder necessary for boot
    try:
        run("arch-chroot /mnt bootctl --path=/boot install")
    except subprocess.CalledProcessError as error:
        print('Unable to install bootloader. Is UEFI activated on your machine?',
              ' Error message: ', error.output)

    # Get the part_uuid of the Linux partition
    try:
        linux_partition_uuid = check_output("blkid -L Arch")
        linux_partition_partuuid = check_output(
            "blkid -s PARTUUID -o value "
            + linux_partition_uuid)
    except subprocess.CalledProcessError as error:
        print('Unable to figure out PARTUUID of your Linux partition. Is it really called `Arch`?',
              ' Error message: ', error.output)

    # Write configuration to boot from the previously
    # found Linux partition
    arch_bootloader_conf = (
        "title Arch Linux\n"
        "linux /vmlinuz-linux\n"
        "initrd /initramfs-linux.img\n"
        "options quiet splash loglevel=3 udev.log-priority=3 vga=current root=PARTUUID="
        + linux_partition_partuuid + " rw")

    with open("/mnt/boot/loader/entries/arch.conf", "w") as file:
        file.write(arch_bootloader_conf)

    # Set the previous configuration as the default to boot
    default_bootloader_conf = (
        "default arch\n"
        "timeout 0\n"
        "editor  0")

    with open("/mnt/boot/loader/loader.conf", "w") as file:
        file.write(default_bootloader_conf)
