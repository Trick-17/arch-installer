from pyscripts.utilities import run
from subprocess import CalledProcessError

def configure_network():
    print(" >> Enabling dhcpd")
    try:
        run('arch-chroot /mnt systemctl enable dhcpcd')
    except CalledProcessError as error:
        print('Enabling dhcpd failed with message: ', error.output)
