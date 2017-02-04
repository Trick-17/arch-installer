import subprocess
from subprocess import run

try:
    run("genfstab -pU /mnt >> /mnt/etc/fstab", shell=True, check=True)
except subprocess.CalledProcessError as error:
    print('Unable to generate /mnt/etc/fstab...',
            ' Error message: ', error.output)
