#!/bin/bash

### Get user input variables
source arch-installer/user-input.txt

### Clone the Prezto files
git clone --recursive https://github.com/sorin-ionescu/prezto.git /mnt/etc/skel/.zprezto

### Set correct theme
sed -i "s|theme '<replace>'|theme '$USER_ZSH_THEME'|g" arch-installer/zsh/zpreztorc

### Copy them into the user's folder
zsh arch-installer/zsh/zsh_setup_configs.sh

### Copy prompt theme and .zpreztorc over
cp arch-installer/zsh/zshrc /mnt/etc/skel/.zshrc
cp arch-installer/zsh/zpreztorc /mnt/etc/skel/.zpreztorc
cp arch-installer/zsh/prompt_josh_setup /mnt/etc/skel/.zprezto/modules/prompt/functions/
cp arch-installer/zsh/prompt_nicholas_setup /mnt/etc/skel/.zprezto/modules/prompt/functions/
cp arch-installer/zsh/prompt_gideon_setup /mnt/etc/skel/.zprezto/modules/prompt/functions/

### Change the default shell
sed -i "s|SHELL=/bin/bash|SHELL=/bin/zsh|g" /mnt/etc/default/useradd

### Add powerline fonts to display prezto symbols
git clone https://github.com/powerline/fonts
export HOME="/mnt/etc/skel"
zsh ./fonts/install.sh