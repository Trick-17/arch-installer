from subprocess import call
from os import chdir
import tarfile

##
## Install Aura

# Download tar-ball
chdir("/home/installer")
call("wget https://aur.archlinux.org/cgit/aur.git/snapshot/aura-bin.tar.gz", shell=True)

# Exctract archive
tar = tarfile.open("aura-bin.tar.gz")
tar.extractall()
tar.close()

# Go into package dir
chdir("aura-bin")
# Build package
call("makepkg", shell=True)
# Call installer for package
call("sudo pacman -U aura-bin*.pkg.tar.xz --noconfirm", shell=True)
# Go out of package dir
chdir("..")



##
## Use Aura to install the rest of the packages

# Open list of packages
with open('aurPackageList.txt') as f:
    # Make list of packages to install
    packages = f.read().replace('\n', ' ')

# Call installer for all packages
call("sudo aura -A "+packages+" --noconfirm", shell=True)
