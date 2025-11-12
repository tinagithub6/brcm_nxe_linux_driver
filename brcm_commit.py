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

parser = argparse.ArgumentParser(description="A simple greeting script.")
parser.add_argument("baseline_branch", type=str, help="The name of the person to greet.")
parser.add_argument("new_branch", type=str, help="The age of the person.")
parser.add_argument("drop_full_path_with_filename", type=str, help="The age of the person.")
componentlist = set()

args = parser.parse_args()

print(f"Hello, baseline_branch: {args.baseline_branch}! You are new_branch: {args.new_branch}. Drop location: {args.drop_full_path_with_filename}")

current_path = os.getcwd()
tool_location = os.getcwd() # C:\Users\choutin\Documents\project\commit_tool_test

# drop_location = args.drop_full_path_with_filename.replace(".zip", "")
# print("drop_location")
# print(drop_location)
# print("ddcccc drop_location")
# path_redefine = '7z x ' +  args.drop_full_path_with_filename + ' -y -o' + drop_location
# path_redefine = path_redefine.replace("\\", "//")
# print(path_redefine)

# now = datetime.now()
# print("before 7z start")
# print(now)
# os.system(path_redefine) #unzip .7z

# end = datetime.now()
# print("before 7z finished")
# print(end)

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
    # os.system(path_redefine) #unzip .7z

    end = datetime.now()
    print("before 7z finished")
    print(end)

    do_Firmware_PLDM_NXE(drop_location, args.baseline_branch, args.new_branch)

    # do_Windows_Drivers_NXE(drop_location, args.baseline_branch, args.new_branch)
    # print("tool_location")
    # print(tool_location)

    # os.chdir(tool_location)
    # do_VMware_Drivers_NXE(drop_location, args.baseline_branch, args.new_branch)

    # os.chdir(tool_location)
    # do_Linux_Drivers_NXE(drop_location, args.baseline_branch, args.new_branch)

    # exit
    # do_Windows_Drivers_NXE()
    # x = threading.Thread(target=do_Linux_Drivers_NXE, args = (drop_location, args.baseline_branch, args.new_branch))
    # logging.info("Main    : before running thread")
    # y = threading.Thread(target=do_Windows_Drivers_NXE, args = (drop_location, args.baseline_branch, args.new_branch))
    # z = threading.Thread(target=do_VMware_Drivers_NXE, args = str(NXE_OPT))
    # z = threading.Thread(target=do_VMware_Drivers_NXE, args = (drop_location, args.baseline_branch, args.new_branch))
    
    # args=("my_string",)).start()
    # threads.append(x)
    # threads.append(y)
    
    # x.start()
    # y.start()

    # z.start()

    # threads = [y, z]

    # while any(t.is_alive() for t in threads):
    #     print("Main thread: Some threads are still running...")
    #     time.sleep(1) # Check every second

    # print("Main thread: All threads have finished.")
    # os.chdir(tool_location + )
    # git_commit_opt_win_drv(args.drop_full_path_with_filename, args.new_branch)

    # repos = ["Broadcom-Optimized-VMware_Drivers_NXE", "Broadcom-Optimized-Windows_Drivers_NXE"]
    # for repo in repos:
    #     os.chdir(tool_location + "//" + repo)
    #     git_commit_opt_win_drv(args.drop_full_path_with_filename, args.new_branch)
