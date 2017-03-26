import fileinput
from shutil import copy2
import subprocess
from subprocess import run

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')

if user_input['desktop'] == 'KDE':

    print(" >> Activating Desktop (sddm)")
    try:
        run("arch-chroot /mnt sddm --example-config > /mnt/etc/sddm.conf", shell=True, check=True)
        #sed_inplace("/mnt/etc/sddm.conf", "^Current=.*", "Current=breeze")
        sed_inplace("/mnt/etc/sddm.conf", "CursorTheme=", "CursorTheme=breeze-dark")
        sed_inplace("/mnt/etc/sddm.conf", "Numlock=none", "Numlock=on")
        run("arch-chroot /mnt systemctl enable sddm", shell=True, check=True)
    except subprocess.CalledProcessError as error:
        print('Enabling sddm failed with message: ', error.output)

    print(" >> Copying Desktop and Shell theme files")
    run("mkdir -p /mnt/etc/skel/.config/gtk-3.0", shell=True, check=True)
    run("mkdir -p /mnt/etc/skel/.local/share/konsole/", shell=True, check=True)
    copy2("arch-installer/configuration_desktop/.config/kdeglobals", "/mnt/etc/skel/.config/")
    copy2("arch-installer/configuration_desktop/.config/konsolerc", "/mnt/etc/skel/.config/")
    copy2("arch-installer/configuration_desktop/.config/yakuakerc", "/mnt/etc/skel/.config/")
    copy2("arch-installer/configuration_desktop/.config/kcminputrc", "/mnt/etc/skel/.config/")
    copy2("arch-installer/configuration_desktop/.local/share/konsole/Default.profile", "/mnt/etc/skel/.local/share/konsole/")
    copy2("arch-installer/configuration_desktop/.local/share/konsole/Dark\ Breeze.colorscheme", "/mnt/etc/skel/.local/share/konsole/")
    copy2("arch-installer/configuration_desktop/.gtkrc-2.0", "/mnt/etc/skel/")
    copy2("arch-installer/configuration_desktop/.config/gtk-3.0/settings.ini", "/mnt/etc/locale.conf")