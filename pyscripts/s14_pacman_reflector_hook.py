pacman_reflector_hook = """[Trigger]
Operation = Upgrade
Type = Package
Target = pacman-mirrorlist

[Action]
Description = Updating pacman-mirrorlist with reflector and removing pacnew...
When = PostTransaction
Depends = reflector
Exec = /usr/bin/env sh -c "reflector --latest 100 --sort rate --protocol https --save /etc/pacman.d/mirrorlist; if [[ -f /etc/pacman.d/mirrorlist.pacnew ]]; then rm /etc/pacman.d/mirrorlist.pacnew; fi"
"""

def configure_pacman_reflector_hook():
    with open('/mnt/etc/pacman.d/hooks/mirrorupgrade.hook', 'w') as txt_file:
        txt_file.write(pacman_reflector_hook)