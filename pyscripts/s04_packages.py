#  !  /usr/bin/env python3
import tempfile
from collections import defaultdict
from subprocess import CalledProcessError
from pyscripts.utilities import run
from pyscripts.utilities import sed_inplace

def install_packages(user_input, install_user_name):

    print(" >> Packages Installation...")
    print("    Your package choices: ", user_input)

    ### All the packages

    misc_packages = ['vim',
                     'vim-supertab',
                     'vim-jedi',
                     'zsh',
                     'powerline-fonts',
                     'p7zip',
                     'unrar',
                     'fortune-mod',
                     'reflector',
                     'tree',
                     'openssh',
                     'networkmanager',
                     'htop',
                     'tmux']
    packages = {
        'minimal': {
            'desktop' : [],
            'server'  : ['docker']},
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
                         'ffmpeg']
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
                        'nextcloud-client',
                        'steam'],
            'server': ['vlc',
                       'steam']}
    }

    graphics_driver_packages = {
        'default': ['mesa', 'mesa-libgl', 'xf86-video-vesa', 'opencl-mesa'],
        'intel':   ['mesa', 'mesa-libgl', 'xf86-video-intel', 'opencl-mesa'],
        'nvidia':  ['nvidia', 'nvidia-libgl', 'opencl-nvidia'],
        'amd':     ['mesa', 'mesa-libgl', 'xf86-video-vesa', 'opencl-mesa'],
        'vbox':    ['virtualbox-guest-modules-arch', 'virtualbox-guest-utils', 'opencl-mesa']}

    server_docker_images = {
        'minimal':   ['nginx'],
        'developer': ['gitlab'],
        'office':    [],
        'media':     ['teamspeak', 'nextcloud']}


    ### Generate the package list
    package_list = misc_packages
    package_list += graphics_driver_packages[user_input['graphics driver']]
    #   Add non-minimal packages to list
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

    ### Generate docker image list
    server_docker_list = []
    #   Add non-minimal images to list
    if 'full' in user_input['packages']:
        for _, value in server_docker_images.items():
            server_docker_list += value
    else:
        for package_type in set(['minimal'] + user_input['packages']):
            server_docker_list += server_docker_images[package_type]

    ### Parallel makepkg
    print(" >> Setting `makepkg` parallel")
    sed_inplace(
        '/etc/makepkg.conf',
        '#MAKEFLAGS="-j2"',
        'MAKEFLAGS="-j$(nproc)"')
    sed_inplace(
        '/mnt/etc/makepkg.conf',
        '#MAKEFLAGS="-j2"',
        'MAKEFLAGS="-j$(nproc)"')
    print(" >> Gave `makepkg` the flag `-j2`")


    ### Install packages using pacaur
    print(" >> Going to install user packages")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', dir='/mnt') as package_file:
        package_string = " ".join(package_list)
        package_file.write(package_string)
        package_file.flush()
        try:
            run('arch-chroot /mnt sudo -u {} pacaur -S --noconfirm --noedit `cat {}`'.format(install_user_name, package_file.name))
        except CalledProcessError as error:
            print('Error installing packages. Message: ', error.output)
    print(" >> Installed user packages")

    ### Pull docker images
    if user_input['system type'] == 'server':
        print(" >> Going to pull docker images")
        try:
            for image in server_docker_list:
                run('arch-chroot /mnt sudo -u {} systemctl start docker'.format(install_user_name))
                run('arch-chroot /mnt sudo -u {} docker pull {}'.format(install_user_name, image))
        except CalledProcessError as error:
            print('Error pulling docker images. Message: ', error.output)
        print(" >> Pulled docker images")


    print(" >> Packages Installation... done")