bash arch-installer/scripts/00-user-input.sh #      | tee /mnt/log_user_input.txt
bash arch-installer/scripts/01-setup-partitions.sh #| tee /mnt/log_setup_partitions.txt
bash arch-installer/scripts/02-setup-packages.sh #  | tee /mnt/log_setup_packages.txt
bash arch-installer/scripts/03-setup-languages.sh # | tee /mnt/log_setup_languages.txt
bash arch-installer/scripts/04-setup-bootloader.sh #| tee /mnt/log_setup_bootloader.txt
bash arch-installer/scripts/05-setup-fstab.sh #     | tee /mnt/log_setup_fstab.txt
bash arch-installer/scripts/06-setup-timezone.sh #  | tee /mnt/log_setup_timezone.txt
bash arch-installer/scripts/07-setup-hostname.sh #  | tee /mnt/log_setup_hostname.txt
bash arch-installer/scripts/08-setup-network.sh #   | tee /mnt/log_setup_network.txt
bash arch-installer/scripts/09-setup-sshd.sh #      | tee /mnt/log_setup_sshd.txt
bash arch-installer/scripts/10-setup-desktop.sh #   | tee /mnt/log_setup_desktop.txt
bash arch-installer/scripts/11-setup-shell.sh #     | tee /mnt/log_setup_shell.txt
bash arch-installer/scripts/12-setup-aur.sh #       | tee /mnt/log_setup_aur.txt
bash arch-installer/scripts/13-setup-users.sh #     | tee /mnt/log_setup_users.txt
# bash arch-installer/scripts/14-setup-personal.sh #  | tee /mnt/log_setup_personal.txt
# bash arch-installer/scripts/15-setup-rootfs.sh #    | tee /mnt/log_setup_rootfs.txt