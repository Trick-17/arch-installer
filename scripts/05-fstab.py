import subprocess
from utilities import run

try:
    run("genfstab -pU /mnt >> /mnt/etc/fstab")
except subprocess.CalledProcessError as error:
    print('Unable to generate /mnt/etc/fstab...',
            ' Error message: ', error.output)
