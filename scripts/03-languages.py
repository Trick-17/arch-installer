import fileinput
from shutil import copyfile

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')

def setup_languages(user_input):
    keyboard = user_input['keyboard layout']
    language = user_input['language']
    
    print(" >> Choosing language and keyboard")
    if keyboard == 'DE - Deutschland':
	    # TODO: loadkeys de-latin1
        sed_inplace("arch-installer/20-keyboard.conf", "<replace>", "de")
	    # TODO: echo KEYMAP=de-latin1 > arch-installer/vconsole.conf
        sed_inplace("/mnt/etc/locale.gen", "#en_DK.UTF-8", "en_DK.UTF-8")
        sed_inplace("/mnt/etc/locale.gen", "#en_GB.UTF-8", "en_GB.UTF-8")
        sed_inplace("arch-installer/configuration_zsh/zshrc", "LANG=<replace>", "LANG=en_DK.UTF-8")
        # TODO: echo LANG=en_DK.UTF-8 > arch-installer/locale.conf
        # TODO: echo LC_TIME=en_GB.UTF-8 >> arch-installer/locale.conf
        
    # TODO: Other keyboard layouts and languages

    print(" >> Setting locale vconsole and keyboard .conf files")
    copyfile("arch-installer/locale.conf", "/mnt/etc/locale.conf")
    copyfile("arch-installer/vconsole.conf", "/mnt/etc/vconsole.conf")
    copyfile("arch-installer/20-keyboard.conf", "/mnt/etc/X11/xorg.conf.d")

    print(" >> Generating locale")
    # TODO: arch-chroot /mnt locale-gen