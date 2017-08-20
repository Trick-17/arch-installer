from os import chdir

from subprocess import call

HOME = '/home/installer'

chdir(HOME)
call('pacman -S yajl expac --noconfirm', shell=True)
call('git clone https://aur.archlinux.org/cower.git', shell=True)
chdir(HOME + '/cower')
call('makepkg', shell=True)
call('sudo pacman -U *.pkg.tar.xz --noconfirm', shell=True)
chdir(HOME)
call('git clone https://aur.archlinux.org/pacaur.git', shell=True)
chdir(HOME + '/pacaur')
call('makepkg')
call('sudo pacman -U *.pkg.tar.xz --noconfirm', shell=True)
chdir(HOME)
call('rm -rf cower pacaur', shell=True)
