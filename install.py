"""
    Installs Arch-Linux when called from a live-iso
"""
import argparse

from pyscripts import s000_detect_hardware as hardware
from pyscripts import s00_user_input as user_input
from pyscripts import s01_partitions as partitions
from pyscripts import s02_basic_arch as basic_arch
from pyscripts import s03_package_manager as package_manager
from pyscripts import s04_packages as packages
from pyscripts import s05_languages as languages
from pyscripts import s06_bootloader as bootloader
from pyscripts import s07_fstab as fstab
from pyscripts import s08_timezone as timezone
from pyscripts import s09_hostname as hostname
from pyscripts import s10_network as network
from pyscripts import s11_sshd as sshd
from pyscripts import s12_desktop as desktop
from pyscripts import s13_shell as shell
from pyscripts import s14_pacman_reflector_hook as pacman_reflector_hook
from pyscripts import s15_users as users

import pyscripts.utilities as install_utilities


print('.... Nice info print ....')

# Allow for additional info being printed during setup
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true',
                   help='Print additional info during setup.')
args = parser.parse_args()
install_utilities.DEBUG = args.debug

if args.debug:
    print('--- Debug info-printing enabled ---')

# Try to auto-detect the hardware currently installed

print('Autodecting hardware...')

detected_hardware = {}
detected_hardware['cpu'] = hardware.get_cpu_vendor_id()
detected_hardware['gpu'] = hardware.get_gpu_vendor()

print('Detected:')
print('Graphics card vendor:  ', detected_hardware['gpu'])
print('Processor vendor:  ', detected_hardware['cpu'])
print('')

ui = user_input.get_user_input(detected_hardware)



partitions.create_and_mount()
basic_arch.install_basic_arch()
with install_utilities.fake_install_user() as user:
    package_manager.install_package_manager(user)
    packages.install_packages(ui, user)
languages.setup_languages(ui)
bootloader.configure_bootloader()
fstab.generate_fstab()
timezone.setup_timezone(ui)
hostname.setup_hostname(ui)
network.configure_network()
sshd.configure_ssh()
desktop.configure_desktop(ui)
shell.configure_shell()
users.configure_users(ui)
pacman_reflector_hook.configure_pacman_reflector_hook()
