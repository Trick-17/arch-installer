from shutil import copy2
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

def install_package_manager(install_user_name):
    print(' >> Going to install package manager')

    # Copy install files to fake install user home directory
    copy2(
        'arch-installer/package_manager/installPackageManager.sh',
        '/mnt/home/{}/'.format(install_user_name))

    # Install aura and AUR packages
    run('arch-chroot /mnt sudo -u {0} sh /home/{0}/installAurPackages.sh'.format(install_user_name))

    print(' >> Installed package manager')
