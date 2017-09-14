from pyscripts.utilities import run
from subprocess import CalledProcessError

def autostart_add_services(user_input):
    print(" >> Adding services to autostart")
    try:
        # networking
        run('arch-chroot /mnt systemctl enable dhcpcd')
        run('arch-chroot /mnt systemctl enable NetworkManager')
        # ssh daemon
        run("arch-chroot /mnt systemctl enable sshd")
        # kde desktop daemon
        if user_input['desktop'] == 'KDE plasma':
            run("arch-chroot /mnt systemctl enable sddm")
        # server docker service
        if user_input['system type'] == 'server':
            run("arch-chroot /mnt systemctl enable docker")
    except CalledProcessError as error:
        print('Adding services to autostart failed with message: ', error.output)