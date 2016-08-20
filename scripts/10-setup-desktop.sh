arch-chroot /mnt sddm --example-config > /mnt/etc/sddm.conf

sed -i 's/Current=maui/Current=breeze/g' /mnt/etc/sddm.conf
sed -i 's/CursorTheme=/CursorTheme=breeze-dark/g' /mnt/etc/sddm.conf
sed -i 's/Numlock=none/Numlock=on/g' /mnt/etc/sddm.conf

arch-chroot /mnt systemctl enable sddm

### Copy GTK theme file s.t. all users automatically have this
cp arch-installer/.gtkrc-2.0 /mnt/etc/skel/

### Copy KDE theme file s.t. all users automatically have this
mkdir -p /mnt/etc/skel/.kde4/share/config/
cp arch-installer/kdeglobals /mnt/etc/skel/.kde4/share/config/kdeglobals_zwei