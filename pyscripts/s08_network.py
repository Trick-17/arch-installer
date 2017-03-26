import subprocess
from subprocess import run

print(" >> Enabling dhcpd")
try:
    run("arch-chroot /mnt systemctl enable dhcpcd", shell=True, check=True)
except subprocess.CalledProcessError as error:
    print('Enabling dhcpd failed with message: ', error.output)
