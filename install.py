"""
    Installs Arch-Linux when called from a live-iso
"""

from pyscripts import s000_detect_hardware as hardware
from pyscripts import s00_user_input as user_input
from pyscripts import s01_partitions as partitions
from pyscripts import s02_packages as packages
from pyscripts import s03_languages as languages
from pyscripts import s04_bootloader as bootloader
from pyscripts import s05_fstab as fstab
from pyscripts import s06_timezone as timezone
from pyscripts import s07_hostname as hostname

cpu = hardware.get_cpu_vendor_id()
gpu_vendor = hardware.get_gpu_vendor()

ui = user_input.get_user_input()

partitions.create_and_mount()

packages.install_packages(ui)

languages.setup_languages(ui)

bootloader.configure_bootloader(ui)

fstab.generate_fstab()

timezone.setup_timezone(ui)

hostname.setup_hostname(ui)