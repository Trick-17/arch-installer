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
        # desktop daemon
        #       kde
        if user_input['desktop'] == 'KDE plasma':
            run("arch-chroot /mnt systemctl enable sddm")
        #       cinnamon
        elif user_input['desktop'] == 'Cinnamon':
            run("arch-chroot /mnt systemctl enable gdm")
        # server docker service
        if user_input['system type'] == 'server':
            run("arch-chroot /mnt systemctl enable docker")
    except CalledProcessError as error:
        print('Adding services to autostart failed with message: ', error.output)