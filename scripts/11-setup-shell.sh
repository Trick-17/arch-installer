### Clone the Prezto files
git clone --recursive https://github.com/sorin-ionescu/prezto.git arch-installer/.zprezto

### Copy them into the user's folder
zsh arch-installer/zsh/zsh_setup_configs.sh

### Copy prompt theme and .zpreztorc over
mkdir -p  /mnt/etc/skel/.zprezto/modules/prompt/functions
cp arch-installer/zsh/zshrc /mnt/etc/skel/.zshrc
cp arch-installer/zsh/zpreztorc /mnt/etc/skel/.zpreztorc
cp arch-installer/zsh/prompt_josh_setup.zsh /mnt/etc/skel/.zprezto/modules/prompt/functions/

### Change the default shell
chsh -s /bin/zsh