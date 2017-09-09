from subprocess import CalledProcessError
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

basics = ['base', 'base-devel', 'sudo', 'wget', 'git']

def install_basic_arch():
    ### Nicer formatting for pacstrap
    sed_inplace("/etc/pacman.conf", "#Color", "Color")
    sed_inplace("/etc/pacman.conf", "#TotalDownload", "TotalDownload")
    ### Enable Multilib
    sed_inplace("/etc/pacman.conf", "#[multilib]", "[multilib]")
    sed_inplace("/etc/pacman.conf", "#Include = /etc/pacman.d/mirrorlist", "Include = /etc/pacman.d/mirrorlist")

    ### Update mirrorlist
    print(" >> Updating mirror list")
    try:
        run('reflector --latest 100 --sort rate --protocol https --save /etc/pacman.d/mirrorlist')
    except CalledProcessError as error:
        print('Updating package mirrorlist failed with message: ', error.output)



    print(" >> Going to install arch base packages")
    try:
        run('pacstrap /mnt '+ ' '.join(basics))
    except CalledProcessError as error:
        print('Error installing base packages. Message: ', error.output)

    print(" >> Installed arch base packages")


    ### Nicer formatting for pacstrap on installed system
    sed_inplace("/mnt/etc/pacman.conf", "#Color", "Color")
    sed_inplace("/mnt/etc/pacman.conf", "#TotalDownload", "TotalDownload")
    ### Enable Multilib on installed system
    sed_inplace("/mnt/etc/pacman.conf", "#[multilib]", "[multilib]")
    sed_inplace("/mnt/etc/pacman.conf", "#Include = /etc/pacman.d/mirrorlist", "Include = /etc/pacman.d/mirrorlist")