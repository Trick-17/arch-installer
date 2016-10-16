#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt


### Place yakuake into autostart
echo " >> Adding yakuake to autostart"
mkdir -p /mnt/etc/skel/.config/autostart-scripts/
chmod +x arch-installer/autostart/yakuake.sh
cp arch-installer/autostart/yakuake.sh /mnt/etc/skel/.config/autostart-scripts/yakuake.sh


echo " >> Installing zsh with prezto"
### Clone the Prezto files
git clone --recursive https://github.com/sorin-ionescu/prezto.git /mnt/etc/skel/.zprezto

### Set correct theme
# sed -i "s|theme '<replace>'|theme '$USER_ZSH_THEME'|g" arch-installer/configuration_zsh/zpreztorc

### Copy them into the user's folder
zsh arch-installer/configuration_zsh/zsh_setup_configs.sh

### Copy prompt theme and .zpreztorc over
cp arch-installer/configuration_zsh/zshrc /mnt/etc/skel/.zshrc
cp arch-installer/configuration_zsh/zpreztorc /mnt/etc/skel/.zpreztorc
cp arch-installer/configuration_zsh/prompt_plasmon_setup /mnt/etc/skel/.zprezto/modules/prompt/functions/

### Copy Vim-config
cp arch-installer/configuration_zsh/.vimrc /mnt/etc/skel/

### Change the default shell
echo " >> Changing default shell to zsh"
sed -i "s|SHELL=/bin/bash|SHELL=/bin/zsh|g" /mnt/etc/default/useradd

### Add powerline fonts to display prezto symbols
echo " >> Installing powerline fonts"
git clone https://github.com/powerline/fonts
export HOME="/mnt/etc/skel"
zsh ./fonts/install.sh
