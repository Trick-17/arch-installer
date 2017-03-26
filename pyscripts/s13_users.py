import fileinput
from shutil import copy2
import subprocess
from subprocess import run

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')

### Add user
username = user_input['username']
run("arch-chroot /mnt useradd -m -G wheel -s /bin/bash "+username, shell=True, check=True)

### Get user password
success = False
while not success:
    try:
        print(" >> Please type in a password for "+username+":")
        run("arch-chroot /mnt passwd "+username, shell=True, check=True)
        success = True
    except subprocess.CalledProcessError as error:
        print(' >> It seems you did not type in matching passwords. Error-message: ', error.output)

### Get root password
success = False
while not success:
    try:
        print(" >> Please type in a password for root user:")
        run("arch-chroot /mnt passwd", shell=True, check=True)
        success = True
    except subprocess.CalledProcessError as error:
        print(' >> It seems you did not type in matching passwords. Error-message: ', error.output)

### Place the user into the sudoers list
sed_inplace("/mnt/etc/sudoers", "# %wheel ALL=(ALL) ALL", "%wheel ALL=(ALL) ALL")
