import subprocess
import fileinput
import re

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
    return subprocess.check_output(command, shell=True).decode("utf-8")
