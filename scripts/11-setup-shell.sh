#!/bin/bash

### Clone the Prezto files
git clone --recursive https://github.com/sorin-ionescu/prezto.git /mnt/etc/skel/.zprezto

### Copy them into the user's folder
zsh arch-installer/zsh/zsh_setup_configs.sh

### Copy prompt theme and .zpreztorc over
cp arch-installer/zsh/zshrc /mnt/etc/skel/.zshrc
cp arch-installer/zsh/zpreztorc /mnt/etc/skel/.zpreztorc
cp arch-installer/zsh/prompt_josh_setup.zsh /mnt/etc/skel/.zprezto/modules/prompt/functions/

### Change the default shell
sed -i "s|SHELL=/bin/bash|SHELL=/bin/zsh|g" /mnt/etc/default/useradd