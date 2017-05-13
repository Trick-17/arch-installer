def get_cpu_vendor_id():
    import re
    with open("/proc/cpuinfo", "r") as myfile:
        cpu_info = myfile.read()
        cpu_vendor_id = re.search('vendor_id\s*\:\s([a-zA-Z0-9]*).*', cpu_info).group(1)

    return cpu_vendor_id

def get_gpu_vendor():
    from pyscripts.utilities import run
    from pyscripts.utilities import check_output
    from subprocess import CalledProcessError

    run("update-pciids")
    vendors = ['VirtualBox Graphics Adapter', 'nvidia', 'intel', 'amd' ]

    for vendor in vendors:
        try:
            output = check_output("lspci | grep -i 'vga.*"+vendor+"\|3d.*"+vendor+"\|2d.*"+vendor+"'")
            if vendor == 'VirtualBox Graphics Adapter':
                return 'vbox'
            else:
                return vendor
        except CalledProcessError:
            pass

    return "default"