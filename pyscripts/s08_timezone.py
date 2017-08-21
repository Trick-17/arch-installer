from subprocess import CalledProcessError
from pyscripts.utilities import run


def setup_timezone(user_input):
    print(' >> Setting Timezone')
    try:
        if user_input['timezone'] == 'Deutschland':
            run('arch-chroot /mnt ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime')
        if user_input['timezone'] == 'Schweiz':
            run('arch-chroot /mnt ln -sf /usr/share/zoneinfo/Europe/Zurich /etc/localtime')
    except CalledProcessError as error:
        print('Unable to set timezone',
            ' Error message: ', error.output)

    print(' >> Setting system clock')
    try:
        run('arch-chroot /mnt hwclock --systohc')
    except CalledProcessError as error:
        print('Unable to set system clock...',
            ' Error message: ', error.output)
