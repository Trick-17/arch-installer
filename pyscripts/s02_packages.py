#  !  /usr/bin/env python3
from collections import defaultdict
from subprocess import CalledProcessError
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

def install_packages(user_input):
    ### Setup Package List
    print(" >> Creating package list")
    print(" Your choices: ", user_input)

    misc_packages = ['base',
                     'base-devel',
                     'sudo',
                     'wget',
                     'git',
                     'vim',
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
                                  'doxygen']),
        'office': defaultdict(lambda:
                              ['texlive-most',
                               'texlive-lang']),
        'media': defaultdict(lambda:
                             ['gnuplot',
                              'graphviz',
                              'ffmpeg'])
    }

    aur_packages = {
        'minimal': {
            'desktop' : [],
            'server'  : []},
        'developer': defaultdict(lambda:
                                 ['clinfo']),
        'office': defaultdict(lambda:
                              []),
        'media': defaultdict(lambda:
                             [])
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
                        'xclip'],
            'server': []},
        'developer': defaultdict(lambda: ['xterm']),
        'office': defaultdict(lambda:
                              ['texstudio',
                               'libreoffice-fresh']),
        'media': {
            'desktop': ['teamspeak3',
                        'gimp',
                        'inkscape',
                        'blender',
                        'handbrake',
                        'vlc'],
            'server': ['vlc',
                       'teamspeak3-server',
                       'nextcloud']}
    }

    aur_gui_packages = {
        'minimal': defaultdict(lambda: ['yakuake-skin-breeze-thin-dark']),
        'developer': defaultdict(lambda: ['visual-studio-code']),
        'office': defaultdict(lambda: []),
        'media': {
            'desktop': ['skypeforlinux-bin', 'nextcloud-client'],
            'server': []}
    }

    graphics_driver_packages = {
        'default': ['mesa', 'mesa-libgl', 'xf86-video-vesa', 'opencl-mesa'],
        'intel':   ['mesa', 'mesa-libgl', 'xf86-video-intel', 'opencl-mesa'],
        'nvidia':  ['nvidia', 'nvidia-libgl', 'opencl-nvidia'],
        'amd':     ['mesa', 'mesa-libgl', 'xf86-video-vesa', 'opencl-mesa'],
        'vbox':    ['virtualbox-guest-modules-arch', 'virtualbox-guest-utils', 'opencl-mesa']}

    package_list = misc_packages
    package_list += graphics_driver_packages[user_input['graphics driver']]

    aur_package_list = []

    if 'full' in user_input['packages']:
        for _, value in packages.items():
            package_list += value[user_input['system type']]
        
        for _, value in aur_packages.items():
            aur_package_list += value[user_input['system type']]


        if user_input['desktop'] != 'none':
            package_list += desktop_distros[user_input['desktop']]
            for _, value in gui_packages.items():
                package_list += value[user_input['system type']]
            for _, value in aur_gui_packages.items():
                aur_package_list += value[user_input['system type']]

    else:
        for package_type in set(['minimal'] + user_input['packages']):
            package_list += packages[package_type][user_input['system type']]
            aur_package_list += aur_packages[package_type][user_input['system type']]

            if user_input['desktop'] != 'none':
                package_list += desktop_distros[user_input['desktop']]
                package_list += gui_packages[package_type][user_input['system type']]
                aur_package_list += aur_gui_packages[package_type][user_input['system type']]

    package_string = " ".join(package_list)
    aur_package_string = " ".join(aur_package_list)

    with open('arch-installer/aur-packages/aurPackageList.txt', 'w') as txt_file:
        txt_file.write(aur_package_string)



    ### Nicer formatting for pacstrap
    sed_inplace("/etc/pacman.conf", "#Color", "Color")
    sed_inplace("/etc/pacman.conf", "#TotalDownload", "TotalDownload")

    ### Update mirrorlist
    print(" >> Updating mirror list")
    try:
        run('reflector --latest 100 --sort rate --protocol https --save /etc/pacman.d/mirrorlist')
    except CalledProcessError as error:
        print('Updating package mirrorlist failed with message: ', error.output)



    print(" >> Going to install arch packages")
    try:
        run('pacstrap /mnt '+ package_string)
    except CalledProcessError as error:
        print('Error installing packages. Message: ', error.output)

    print(" >> Installed arch packages")


    ### Nicer formatting for pacstrap on installed system
    sed_inplace("/mnt/etc/pacman.conf", "#Color", "Color")
    sed_inplace("/mnt/etc/pacman.conf", "#TotalDownload", "TotalDownload")
