import os
import fileinput
from shutil import copy2
from subprocess import CalledProcessError
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

def set_keymap(keymap):
    with open('/mnt/etc/vconsole.conf', 'w') as text_file:
        text_file.write('KEYMAP='+keymap)


def set_keymap_gui(keymap_gui, internationalisation=False):
    # Set the keymap
    sed_inplace('arch-installer/20-keyboard.conf', '<LAYOUT>', keymap_gui)

    # If internationalisation is chosen, add the option
    if internationalisation:
        sed_inplace('arch-installer/20-keyboard.conf', '<INTL>',
                    'Option          \"XkbVariant\" \"altgr-intl\"')
    else:
        sed_inplace('arch-installer/20-keyboard.conf', '<INTL>', '')

    # Finally copy file over
    run("mkdir -p /mnt/etc/X11/xorg.conf.d/")
    copy2('arch-installer/20-keyboard.conf', '/mnt/etc/X11/xorg.conf.d/')

def set_locale(lang, lc_time):
    with open('/mnt/etc/locale.conf', 'w') as text_file:
        text_file.write('LANG=' + lang + '\n')
        text_file.write('LC_TIME=' + lc_time + '\n')
        sed_inplace('/mnt/etc/locale.gen', '#' + lang, lang)
        sed_inplace('/mnt/etc/locale.gen', '#' + lc_time, lc_time)
        sed_inplace('arch-installer/configuration_zsh/zshrc', '<replace>',  lang)

def setup_languages(user_input):
    keyboard = user_input['keyboard layout']
    language = user_input['language']
    has_gui = user_input['desktop'] == 'KDE plasma'

    print(" >> Setting language and keyboard layout")
    if language == 'english (reasonable)':
        set_locale('en_DK.UTF-8', 'en_GB.UTF-8')
    elif language == 'english (US)':
        set_locale('en_US.UTF-8', 'en_US.UTF-8')

    if keyboard == 'DE - Deutschland':
        set_keymap('de-latin1')
        if has_gui:
            set_keymap_gui('de')

    elif keyboard == 'DE - Schweiz':
        set_keymap('sg-latin1')
        if has_gui:
            set_keymap_gui('ch')

    if keyboard == 'EN - US':
        set_keymap('us')
        if has_gui:
            set_keymap_gui('us', True)

    if keyboard == 'EN - GB':
        set_keymap('gb')
        if has_gui:
            set_keymap_gui('gb', True)

    try:
        print(" >> Generating locale")
        run("arch-chroot /mnt locale-gen")
    except CalledProcessError as error:
        print('Unable to generate locale on /mnt...',
              ' Error message: ', error.output)
