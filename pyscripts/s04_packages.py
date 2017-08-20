#  !  /usr/bin/env python3
import tempfile
from collections import defaultdict
from subprocess import CalledProcessError
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

def install_packages(user_input, install_user_name):
    ### Setup Package List
    print(" >> Creating package list")
    print(" Your choices: ", user_input)

    misc_packages = ['vim',
                     'vim-supertab',
                     'vim-jedi',
                     'zsh',
                     'powerline-fonts',
                     'p7zip',
                     'unrar',
                     'fortune-mod',
                     'reflector',
                     'tree']
    packages = {
        'minimal': {
            'desktop' : [],
            'server'  : ['openssh']},
        'developer': defaultdict(lambda:
                                 ['cmake',
                                  'boost',
                                  'eigen',
                                  'opencl-headers',
                                  'ocl-icd',
                                  'openmpi',
                                  'hdf5-cpp-fortran',
                                  'python2-pip',
                                  'python-pip',
                                  'ipython',
                                  'python-h5py',
                                  'python-scipy',
                                  'python-matplotlib',
                                  'python-pillow',
                                  'python-pylint',
                                  'autopep8',
                                  'doxygen',
                                  'clinfo']),
        'office': defaultdict(lambda:
                              ['texlive-most',
                               'texlive-lang']),
        'media': {
            'desktop' : ['gnuplot',
                         'graphviz',
                         'ffmpeg'],
            'server'  : ['gnuplot',
                         'graphviz',
                         'ffmpeg',
                         'teamspeak3-server']
        }
    }

    desktop_distros = {
        "KDE plasma": ['xorg-server',
                       'xorg-apps',
                       'yakuake',
                       'plasma-meta',
                       'kde-applications']
    }

    gui_packages = {
        'minimal': {
            'desktop': ['qtox',
                        'xclip',
                        'yakuake-skin-breeze-thin-dark'],
            'server': ['yakuake-skin-breeze-thin-dark']},
        'developer': defaultdict(lambda: ['xterm', 'visual-studio-code']),
        'office': defaultdict(lambda:
                              ['texstudio',
                               'libreoffice-fresh']),
        'media': {
            'desktop': ['teamspeak3',
                        'gimp',
                        'inkscape',
                        'blender',
                        'handbrake',
                        'vlc',
                        'skypeforlinux-bin',
                        'nextcloud-client'],
            'server': ['vlc',
                       'nextcloud']}
    }

    graphics_driver_packages = {
        'default': ['mesa', 'mesa-libgl', 'xf86-video-vesa', 'opencl-mesa'],
        'intel':   ['mesa', 'mesa-libgl', 'xf86-video-intel', 'opencl-mesa'],
        'nvidia':  ['nvidia', 'nvidia-libgl', 'opencl-nvidia'],
        'amd':     ['mesa', 'mesa-libgl', 'xf86-video-vesa', 'opencl-mesa'],
        'vbox':    ['virtualbox-guest-modules-arch', 'virtualbox-guest-utils', 'opencl-mesa']}

    package_list = misc_packages
    package_list += graphics_driver_packages[user_input['graphics driver']]

    if 'full' in user_input['packages']:
        for _, value in packages.items():
            package_list += value[user_input['system type']]
        
        if user_input['desktop'] != 'none':
            package_list += desktop_distros[user_input['desktop']]
            for _, value in gui_packages.items():
                package_list += value[user_input['system type']]

    else:
        for package_type in set(['minimal'] + user_input['packages']):
            package_list += packages[package_type][user_input['system type']]

            if user_input['desktop'] != 'none':
                package_list += desktop_distros[user_input['desktop']]
                package_list += gui_packages[package_type][user_input['system type']]

    package_string = " ".join(package_list)

    print(" >> Going to install user packages")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', dir='/mnt') as package_file:
        package_file.write(package_string)
        package_file.flush()
        try:
            run('arch-chroot /mnt sudo -u {} pacaur -S --noconfirm `cat {}`'.format(install_user_name, package_file.name))
        except CalledProcessError as error:
            print('Error installing packages. Message: ', error.output)

    print(" >> Installed user packages")
