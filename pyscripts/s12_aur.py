from shutil import copy2
from subprocess import run

print(" >> Going to install AUR packages")

# Create fake install user
run("arch-chroot /mnt useradd -m installer", shell=True, check=True)
open('/mnt/etc/sudoers', 'a').write('installer ALL=(ALL) NOPASSWD: ALL\n')

# Copy install files to fake install user home directory
copy2("arch-installer/aur-packages/aurPackageList.txt", "/mnt/home/installer/")
copy2("arch-installer/aur-packages/installAurPackages.py", "/mnt/home/installer/")

# Install aura and AUR packages
run("arch-chroot /mnt sudo -u installer python /home/installer/installAurPackages.py", shell=True, check=True)

# Remove fake install user,
run("arch-chroot /mnt userdel installer", shell=True, check=True)
# TODO:
#sed -i '/installer ALL=(ALL) NOPASSWD: ALL/d' /mnt/etc/sudoers
run("rm -rf /mnt/home/installer", shell=True, check=True)

print(" >> Installed AUR packages")