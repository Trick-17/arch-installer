import fileinput
from shutil import copyfile
from subprocess import run

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')

def setup_languages(user_input):
    keyboard = user_input['keyboard layout']
    language = user_input['language']
    
    print(" >> Choosing language and keyboard")
    if keyboard == 'DE - Deutschland':
        run("loadkeys de-latin1", shell=True)
        open('arch-installer/vconsole.conf', 'w').write('KEYMAP=de-latin1\n')
        open('arch-installer/locale.conf', 'w').write('LANG=en_DK.UTF-8\n')
        open('arch-installer/locale.conf', 'a').write('LC_TIME=en_GB.UTF-8\n')
        sed_inplace("/mnt/etc/locale.gen", "#en_DK.UTF-8", "en_DK.UTF-8")
        sed_inplace("/mnt/etc/locale.gen", "#en_GB.UTF-8", "en_GB.UTF-8")
        sed_inplace("arch-installer/20-keyboard.conf", "<replace>", "de")
        sed_inplace("arch-installer/configuration_zsh/zshrc", "LANG=<replace>", "LANG=en_DK.UTF-8")
        
    if keyboard == 'DE - Schweiz':
        run("loadkeys sg-latin1", shell=True)
        open('arch-installer/vconsole.conf', 'w').write('KEYMAP=sg-latin1\n')
        open('arch-installer/locale.conf', 'w').write('LANG=en_DK.UTF-8\n')
        open('arch-installer/locale.conf', 'a').write('LC_TIME=en_GB.UTF-8\n')
        sed_inplace("/mnt/etc/locale.gen", "#en_DK.UTF-8", "en_DK.UTF-8")
        sed_inplace("/mnt/etc/locale.gen", "#en_GB.UTF-8", "en_GB.UTF-8")
        sed_inplace("arch-installer/20-keyboard.conf", "<replace>", "ch")
        sed_inplace("arch-installer/configuration_zsh/zshrc", "LANG=<replace>", "LANG=en_DK.UTF-8")

    if keyboard == 'EN - DK':
        open('arch-installer/vconsole.conf', 'w').write('KEYMAP=us\n')
        open('arch-installer/locale.conf', 'w').write('LANG=en_DK.UTF-8\n')
        sed_inplace("/mnt/etc/locale.gen", "#en_DK.UTF-8", "en_DK.UTF-8")
        sed_inplace("arch-installer/20-keyboard.conf", "<replace>", "us")
        sed_inplace("arch-installer/configuration_zsh/zshrc", "LANG=<replace>", "LANG=en_DK.UTF-8")

    if keyboard == 'EN - US':
        open('arch-installer/vconsole.conf', 'w').write('KEYMAP=us\n')
        open('arch-installer/locale.conf', 'w').write('LANG=en_US.UTF-8\n')
        sed_inplace("/mnt/etc/locale.gen", "#en_US.UTF-8", "en_US.UTF-8")
        sed_inplace("arch-installer/20-keyboard.conf", "<replace>", "us")
        sed_inplace("arch-installer/configuration_zsh/zshrc", "LANG=<replace>", "LANG=en_US.UTF-8")


    print(" >> Setting locale vconsole and keyboard .conf files")
    copyfile("arch-installer/locale.conf", "/mnt/etc/locale.conf")
    copyfile("arch-installer/vconsole.conf", "/mnt/etc/vconsole.conf")
    copyfile("arch-installer/20-keyboard.conf", "/mnt/etc/X11/xorg.conf.d")

    try:
        print(" >> Generating locale")
        run("arch-chroot /mnt locale-gen", shell=True, check=True)
    except subprocess.CalledProcessError as error:
        print('Unable to generate locale on /mnt...',
              ' Error message: ', error.output)