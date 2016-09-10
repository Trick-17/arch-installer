from subprocess import Popen
from subprocess import call
from os import chdir
import tarfile


def install_pkg(package):
    # Go into package dir
    chdir(package)
    # Install package
    call("pacman -U "+package+"*.pkg.tar.xz --noconfirm", shell=True)
    # Go out of package dir
    chdir("..")




# Loop over packages
with open('aurPackageList.txt') as f:
    chdir("install")
    packages = [line.strip() for line in f]
    for package in packages:
        install_pkg(package)

# Note: vs code depends on gconf
#       yaourt depends on yajl