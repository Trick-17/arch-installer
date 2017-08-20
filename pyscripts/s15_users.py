import fileinput
from shutil import copy2
import subprocess
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

def configure_users(user_input):
    ### Add user
    username = user_input['username']
    run("arch-chroot /mnt useradd -m -G wheel -s /bin/bash "+username)

    ### Get user password
    success = False
    while not success:
        try:
            print(" >> Please type in a password for "+username+":")
            run("arch-chroot /mnt passwd "+username)
            success = True
        except subprocess.CalledProcessError as error:
            print(' >> It seems you did not type in matching passwords. Error-message: ', error.output)

    ### Get root password
    success = False
    while not success:
        try:
            print(" >> Please type in a password for root user:")
            run("arch-chroot /mnt passwd")
            success = True
        except subprocess.CalledProcessError as error:
            print(' >> It seems you did not type in matching passwords. Error-message: ', error.output)

    ### Place the user into the sudoers list
    sed_inplace("/mnt/etc/sudoers", "# %wheel ALL=\(ALL\) ALL", "%wheel ALL=(ALL) ALL")
