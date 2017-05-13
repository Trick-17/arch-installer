from subprocess import CalledProcessError
from pyscripts.utilities import run

def generate_fstab():
    try:
        run("genfstab -pU /mnt >> /mnt/etc/fstab")
    except CalledProcessError as error:
        print('Unable to generate /mnt/etc/fstab...',
                ' Error message: ', error.output)
