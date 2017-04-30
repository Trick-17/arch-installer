from pyscripts.utilities import run
from subprocess import CalledProcessError

print(" >> Enabling sshd")
try:
    run("arch-chroot /mnt systemctl enable sshd")
except CalledProcessError as error:
    print('Enabling sshd failed with message: ', error.output)
