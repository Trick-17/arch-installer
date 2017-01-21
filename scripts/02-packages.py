#  !  /usr/bin/env python3
import fileinput

def sed_inplace(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')


### Nicer formatting for pacstrap
sed_inplace("/etc/pacman.conf", "#Color", "Color")
sed_inplace("/etc/pacman.conf", "#TotalDownload", "TotalDownload")

### Update mirrorlist
print(" >> Updating mirror list")
# reflector --verbose --latest 40 --sort rate --protocol https --save /etc/pacman.d/mirrorlist

### Setup Package List
print(" >> Creating package list")
packages = {
    'desktop': {
        'minimal':       [],
        'developer':     ['cmake','gnuplot','boost','eigen','ocl-icd','opencl-headers','openmpi','hdf5-cpp-fortran','python-pip','ipython','python-h5py','python-scipy','python-matplotlib','python-pillow','python-pylint','tree'],
        'developer_tex': ['texlive-most','texlive-lang'],
        'media':         [],
        'full':          ['doxygen','graphviz'],
    },
    'server': {
        'minimal':       [],
        'developer':     ['cmake','boost','eigen'],
        'developer_tex': ['texlive-most','texlive-lang'],
        'media':         [],
        'full':          ['doxygen','graphviz']
    },
    'gui': {
        'desktop': {
            'minimal':       ['chromium','thunderbird','qtox','owncloud-client'],
            'developer':     ['filezilla','gimp','inkscape'],
            'developer_tex': ['texstudio'],
            'media':         ['vlc','teamspeak3'],
            'full':          ['texstudio']
        },
        'server': {
            'minimal':       ['chromium'],
            'developer':     [],
            'developer_tex': [],
            'media':         ['vlc','teamspeak3-server','owncloud-server'],
            'full':          []
        },
        'kde': ['yakuake','plasma-meta','kde-applications']
    },
    'graphics_drivers': {
        'default': ['mesa','mesa-libgl','xf86-video-vesa','opencl-mesa'],
        'intel':   ['mesa','mesa-libgl','xf86-video-intel','opencl-mesa'],
        'nvidia':  ['nvidia','nvidia-libgl','opencl-nvidia'],
        'amd':     ['mesa','mesa-libgl','xf86-video-vesa','opencl-mesa'],
        'vbox':    ['virtualbox-guest-modules-arch','virtualbox-guest-utils','opencl-mesa']
    },
    'aur_dependencies': ['abs']
}


print(" >> Going to install arch packages")
# pacstrap /mnt base base-devel intel-ucode \
#               sudo wget openssh git vim zsh powerline-fonts archiso p7zip unrar xclip fortune-mod reflector \
#               $packages_user $packages_graphics abs
print(" >> Installed arch packages")


### Nicer formatting for pacstrap on installed
sed_inplace("/mnt/etc/pacman.conf", "#Color", "Color")
sed_inplace("/mnt/etc/pacman.conf", "#TotalDownload", "TotalDownload")