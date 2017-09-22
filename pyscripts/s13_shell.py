import os
import fileinput
from shutil import copy2
from subprocess import CalledProcessError
from pyscripts.utilities import sed_inplace
from pyscripts.utilities import run

def configure_shell():
    ### Place yakuake into autostart
    print(" >> Adding yakuake to autostart")
    run("mkdir -p /mnt/etc/skel/.config/autostart-scripts/")
    run("chmod +x arch-installer/autostart/yakuake.sh")
    copy2("arch-installer/autostart/yakuake.sh", "/mnt/etc/skel/.config/autostart-scripts/")


    ### Install zsh and configure
    print(" >> Installing zsh with prezto")

    ### Copy prompt theme and .zpreztorc over
    copy2("arch-installer/configuration_zsh/zshrc", "/mnt/etc/skel/.zshrc")
    copy2("arch-installer/configuration_zsh/zpreztorc", "/mnt/etc/skel/.zpreztorc")

    directory = "/mnt/etc/skel/.zprezto/modules/prompt/functions/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    copy2("arch-installer/configuration_zsh/prompt_plasmon_setup", directory)

    ### Copy Vim-config
    copy2("arch-installer/configuration_zsh/.vimrc", "/mnt/etc/skel/")

    ### Change the default shell
    print(" >> Changing default shell to zsh")
    sed_inplace("/mnt/etc/default/useradd", "SHELL=/bin/bash", "SHELL=/bin/zsh")
