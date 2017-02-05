import subprocess
from subprocess import run

print(" >> Enabling sshd")
try:
    run("arch-chroot /mnt systemctl enable sshd", shell=True, check=True)
except subprocess.CalledProcessError as error:
    print('Enabling sshd failed with message: ', error.output)
