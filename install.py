"""
    Installs Arch-Linux when called from a live-iso
"""
import argparse

from pyscripts import s000_detect_hardware as hardware
from pyscripts import s00_user_input as user_input
from pyscripts import s01_partitions as partitions
from pyscripts import s02_packages as packages
from pyscripts import s03_languages as languages
from pyscripts import s04_bootloader as bootloader
from pyscripts import s05_fstab as fstab
from pyscripts import s06_timezone as timezone
from pyscripts import s07_hostname as hostname
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

packages.install_packages(ui)

languages.setup_languages(ui)

bootloader.configure_bootloader()

fstab.generate_fstab()

timezone.setup_timezone(ui)

hostname.setup_hostname(ui)