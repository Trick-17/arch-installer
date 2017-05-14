from shutil import copy2
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace


def configure_aur():
    print(" >> Going to install AUR packages")

    # Create fake install user
    run("arch-chroot /mnt useradd -m installer")
    open('/mnt/etc/sudoers', 'a').write('installer ALL=(ALL) NOPASSWD: ALL\n')

    # Copy install files to fake install user home directory
    copy2("arch-installer/aur-packages/aurPackageList.txt", "/mnt/home/installer/")
    copy2("arch-installer/aur-packages/installAurPackages.py", "/mnt/home/installer/")

    # Install aura and AUR packages
    run("arch-chroot /mnt sudo -u installer python /home/installer/installAurPackages.py")

    # Remove fake install user,
    run("arch-chroot /mnt userdel installer")
    sed_inplace('/mnt/etc/sudoers', 'installer ALL=\(ALL\) NOPASSWD: ALL', '')
    run("rm -rf /mnt/home/installer")

    print(" >> Installed AUR packages")