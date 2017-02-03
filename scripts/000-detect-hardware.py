def get_cpu_vendor_id():
    import fileinput
    with open("/proc/cpuinfo", "r") as myfile:
        for line in myfile:
            arr_line = line.split(':')
            if arr_line[0] == 'vendor_id':
                cpu_vendor_id = arr_line[1]
        return cpu_vendor_id

def get_gpu_vendor():
    from subprocess import run
    from subprocess import check_output
    run("update-pciids", shell=True)
    if check_output("lspci | grep -i --color 'vga.*virtual\|3d.*virtual\|2d.*virtual'", shell=True) != "":
        return "VirtualBox"
    if check_output("lspci | grep -i --color 'vga.*nvidia\|3d.*nvidia\|2d.*nvidia'", shell=True) != "":
        return "VirtualBox"
    if check_output("lspci | grep -i --color 'vga.*intel\|3d.*intel\|2d.*intel'", shell=True) != "":
        return "VirtualBox"
    if check_output("lspci | grep -i --color 'vga.*amd\|3d.*amd\|2d.*amd'", shell=True) != "":
        return "VirtualBox"