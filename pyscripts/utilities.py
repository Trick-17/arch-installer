import subprocess
import fileinput
import re
import contextlib

DEBUG = False

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(re.sub(textToSearch, textToReplace, line), end='')

def run(command):
    if DEBUG:
        subprocess.run(command + '> /dev/null 2>&1', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
    else:
        subprocess.run(command, shell=True, check=True)

def check_output(command):
    return subprocess.check_output(command, shell=True).decode("utf-8").strip()

@contextlib.contextmanager
def fake_install_user():
    user_name = 'installer'
    run('arch-chroot /mnt useradd -m '+user_name)
    open('/mnt/etc/sudoers', 'a').write(
        '{} ALL=(ALL) NOPASSWD: ALL\n'.format(user_name))
    
    yield user_name

    run('arch-chroot /mnt userdel installer')
    sed_inplace('/mnt/etc/sudoers', 'installer ALL=\(ALL\) NOPASSWD: ALL', '')
    run('rm -rf /mnt/home/installer')
