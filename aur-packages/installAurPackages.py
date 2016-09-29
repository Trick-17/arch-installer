from subprocess import call
from os import chdir
import tarfile

##
## Install Aura

# Download tar-ball
chdir("~")
call("wget https://aur.archlinux.org/cgit/aur.git/snapshot/aura.tar.gz", shell=True)

# Exctract archive
tar = tarfile.open("aura.tar.gz")
tar.extractall()
tar.close()

# Go into package dir
chdir("aura")
# Build package
call("makepkg", shell=True)
# Call installer for package
call("sudo pacman -U aura*.pkg.tar.xz --noconfirm", shell=True)
# Go out of package dir
chdir("..")



##
## Use Aura to install the rest of the packages

# Open list of packages
with open('aurPackageList.txt') as f:
    # Make list of packages to install
    packages = [line.strip() for line in f]
    # Call installer for each package
    for package in packages:
        call("sudo aura -A "+package+"*.pkg.tar.xz --noconfirm", shell=True)