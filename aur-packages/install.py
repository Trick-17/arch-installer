from subprocess import Popen
from subprocess import call
from os import chdir
import tarfile


def build_pkg(package):
    # Download archive (from AUR)
    call("wget https://aur.archlinux.org/cgit/aur.git/snapshot/"+package+".tar.gz", shell=True)

    # Exctract archive
    # call("tar -xzvf "+package+".tar.gz", shell=True)
    tar = tarfile.open(package+".tar.gz")
    tar.extractall()
    tar.close()
    
    # Write permissions
    call("chgrp nobody "+package, shell=True)
    call("chmod g+ws "+package, shell=True)
    call("setfacl -m u::rwx,g::rwx "+package, shell=True)
    call("setfacl -d --set u::rwx,g::rwx,o::- "+package, shell=True)

    # Go into package dir
    chdir(package)
    # call("cd "+package, shell=True)
    # Build package
    call("sudo -u nobody makepkg -s", shell=True)
    # Install package
    call("sudo pacman -U "+package+"*.pkg.tar.xz --noconfirm", shell=True)
    # Go out of package dir
    chdir("..")
    # call("cd ..", shell=True)



# Go into working directory
chdir("/tmp")
call("mkdir install_aur_packages", shell=True)
chdir("install_aur_packages")
# call("pwd", shell=True)

# Loop over packages
for package in ["package-query", "yaourt", "visual-studio-code"]:
    # Build the package
    build_pkg(package)

# Note: vs code depends on gconf
#       yaourt depends on yajl