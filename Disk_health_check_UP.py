#!/usr/bin/env python3
#python -m pip install module_name to download pip from pypl


import shutil
import psutil

def checK_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return  free > 20
def check_cpu_usage():
    usage=psutil.cpu_precent(1)
    return usage < 75

if not checK_disk_usage("/") or not check_cpu_usage:
    print("Error")
else:
    print("Everthing is OK") 
