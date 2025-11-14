import yaml
import subprocess
import os
import argparse
import threading
import time
from datetime import datetime
from brcm_opt_VMware_Drivers_NXE import do_VMware_Drivers_NXE
from brcm_opt_Linux_Drivers_NXE import do_Linux_Drivers_NXE
from brcm_opt_Windows_Drivers_NXE import do_Windows_Drivers_NXE
from brcm_opt_Firmware_PLDM_NXE import do_Firmware_PLDM_NXE
from brcm_opt_Firmware_NXE import do_Firmware_NXE

parser = argparse.ArgumentParser(description="A simple greeting script.")
parser.add_argument("baseline_branch", type=str, help="The name of the person to greet.")
parser.add_argument("new_branch", type=str, help="The age of the person.")
parser.add_argument("drop_full_path_with_filename", type=str, help="The age of the person.")
componentlist = set()

args = parser.parse_args()

print(f"Hello, baseline_branch: {args.baseline_branch}! You are new_branch: {args.new_branch}. Drop location: {args.drop_full_path_with_filename}")

current_path = os.getcwd()
tool_location = os.getcwd() # C:\Users\choutin\Documents\project\commit_tool_test

if __name__ == "__main__":
    threads = list()
    print("eeee")
    drop_location = args.drop_full_path_with_filename.replace(".zip", "")
    print("drop_location")
    print(drop_location)
    print("ddcccc drop_location")
    path_redefine = '7z x ' +  args.drop_full_path_with_filename + ' -y -o' + drop_location
    path_redefine = path_redefine.replace("\\", "//")
    print(path_redefine)

    now = datetime.now()
    print("before 7z start")
    print(now)
    os.system(path_redefine) #unzip .7z

    end = datetime.now()
    print("before 7z finished")
    print(end)

    os.chdir(tool_location)
    do_Linux_Drivers_NXE(drop_location, args.baseline_branch, args.new_branch)

    os.chdir(tool_location)
    do_Windows_Drivers_NXE(drop_location, args.baseline_branch, args.new_branch)

    os.chdir(tool_location)
    do_VMware_Drivers_NXE(drop_location, args.baseline_branch, args.new_branch)

    os.chdir(tool_location)
    do_Firmware_NXE(drop_location, args.baseline_branch, args.new_branch)

    os.chdir(tool_location)
    do_Firmware_PLDM_NXE(drop_location, args.baseline_branch, args.new_branch)
