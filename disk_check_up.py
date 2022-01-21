import shutil as sh #module used to check data usage
disk=sh.disk_usage("/")
print(disk)
disk.free/disk.total*100
import psutil as psh #module used to check processor usage
psh.cpu_present(0.1)

