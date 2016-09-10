from subprocess import Popen
from subprocess import call
from os import chdir
import tarfile


def build_pkg(package):
    # Download archive (from AUR)
    call("wget https://aur.archlinux.org/cgit/aur.git/snapshot/"+package+".tar.gz", shell=True)

    # Exctract archive
    tar = tarfile.open(package+".tar.gz")
    tar.extractall()
    tar.close()
    
    # Go into package dir
    chdir(package)
    # Build package
    call("makepkg", shell=True)
    # Go out of package dir
    chdir("..")




# Loop over packages
with open('aurPackageList.txt') as f:
    chdir("install")
    packages = [line.strip() for line in f]
    for package in packages:
        build_pkg(package)

# Note: vs code depends on gconf
#       yaourt depends on yajl