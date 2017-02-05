import fileinput
from shutil import copy2
import subprocess
from subprocess import run

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')


### Place yakuake into autostart
print(" >> Adding yakuake to autostart")
run("mkdir -p /mnt/etc/skel/.config/autostart-scripts/", shell=True, check=True)
run("chmod +x arch-installer/autostart/yakuake.sh", shell=True, check=True)
copy2("arch-installer/autostart/yakuake.sh", "/mnt/etc/skel/.config/autostart-scripts/")


### Install zsh and configure
print(" >> Installing zsh with prezto")

### Clone the Prezto files
run("git clone --recursive https://github.com/sorin-ionescu/prezto.git /mnt/etc/skel/.zprezto", shell=True, check=True)

### Set correct theme
# sed -i "s|theme '<replace>'|theme '$USER_ZSH_THEME'|g" arch-installer/configuration_zsh/zpreztorc

### Copy them into the user's folder
run("zsh arch-installer/configuration_zsh/zsh_setup_configs.sh", shell=True, check=True)

### Copy prompt theme and .zpreztorc over
copy2("arch-installer/configuration_zsh/zshrc", "/mnt/etc/skel/.zshrc")
copy2("arch-installer/configuration_zsh/zpreztorc", "/mnt/etc/skel/.zpreztorc")
copy2("arch-installer/configuration_zsh/prompt_plasmon_setup", "/mnt/etc/skel/.zprezto/modules/prompt/functions/")

### Add powerline fonts to display prezto symbols
print(" >> Installing powerline fonts")
run("git clone https://github.com/powerline/fonts", shell=True, check=True)
run("export HOME='/mnt/etc/skel' && zsh ./fonts/install.sh", shell=True, check=True)


### Copy Vim-config
copy2("arch-installer/configuration_zsh/.vimrc", "/mnt/etc/skel/")


### Change the default shell
print(" >> Changing default shell to zsh")
sed_inplace("/mnt/etc/default/useradd", "SHELL=/bin/bash", "SHELL=/bin/zsh")
