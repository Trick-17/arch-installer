echo "Please choose your keyboard-layout:"
select yn in "DE - Deutschland" "DE - Schweiz" "EN - US"; do
    case $yn in
        1 ) loadkeys de-latin1 ; echo KEYMAP=de-latin1 > arch-installer/vconsole.conf ; echo LANG=de_DE.UTF-8 > arch-installer/locale.conf; break;;
        2 ) loadkeys sg-latin1; echo KEYMAP=sg-latin1 > arch-installer/vconsole.conf ; echo LANG=de_CH.UTF-8 > arch-installer/locale.conf ; break;;
        3 ) echo LANG=en_US.UTF-8 > arch-installer/locale.conf ; break;;
    esac
done
