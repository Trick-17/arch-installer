import subprocess
import fileinput

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')

def run(command):
    subprocess.run(command, shell=True, check=True)

def check_output(command):
    return subprocess.check_output(command, shell=True, check=True).decode("utf-8")