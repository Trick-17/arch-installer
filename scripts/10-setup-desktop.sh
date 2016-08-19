arch-chroot /mnt sddm --example-config > /mnt/etc/sddm.conf

sed -i 's/Current=maui/Current=breeze/g' /mnt/etc/sddm.conf
sed -i 's/CursorTheme=/CursorTheme=breeze-dark/g' /mnt/etc/sddm.conf
sed -i 's/Numlock=none/Numlock=on/g' /mnt/etc/sddm.conf

arch-chroot /mnt systemctl enable sddm