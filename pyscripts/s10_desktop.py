import os
from shutil import copy2
from shutil import copytree
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace
from subprocess import CalledProcessError


def configure_desktop(user_input):
    if user_input['desktop'] == 'KDE plasma':

        print(" >> Activating Desktop (sddm)")
        try:
            run("arch-chroot /mnt sddm --example-config > /mnt/etc/sddm.conf")
            sed_inplace("/mnt/etc/sddm.conf", "^Current=.*", "Current=breeze")
            sed_inplace("/mnt/etc/sddm.conf", "CursorTheme=", "CursorTheme=breeze-dark")
            sed_inplace("/mnt/etc/sddm.conf", "Numlock=none", "Numlock=on")
            run("arch-chroot /mnt systemctl enable sddm")
        except CalledProcessError as error:
            print('Enabling sddm failed with message: ', error.output)

        print(" >> Copying Desktop and Shell theme files")
        #if not os.path.exists("/mnt/etc/skel/.config/gtk-3.0"):
        #    os.makedirs("/mnt/etc/skel/.config/gtk-3.0")
        #if not os.path.exists("mkdir -p /mnt/etc/skel/.local/share/konsole/"):
        #    os.makedirs("mkdir -p /mnt/etc/skel/.local/share/konsole/")

        copytree("arch-installer/configuration_desktop", "/mnt/etc/skel/")
        #copy2("arch-installer/configuration_desktop/.config/kdeglobals", "/mnt/etc/skel/.config/")
        #copy2("arch-installer/configuration_desktop/.config/konsolerc", "/mnt/etc/skel/.config/")
        #copy2("arch-installer/configuration_desktop/.config/yakuakerc", "/mnt/etc/skel/.config/")
        #copy2("arch-installer/configuration_desktop/.config/kcminputrc", "/mnt/etc/skel/.config/")
        #copy2("arch-installer/configuration_desktop/.local/share/konsole/Default.profile", "/mnt/etc/skel/.local/share/konsole/")
        #copy2("arch-installer/configuration_desktop/.local/share/konsole/Dark Breeze.colorscheme", "/mnt/etc/skel/.local/share/konsole/")
        #copy2("arch-installer/configuration_desktop/.gtkrc-2.0", "/mnt/etc/skel/")
        #copy2("arch-installer/configuration_desktop/.config/gtk-3.0/settings.ini", "/mnt/etc/locale.conf/")