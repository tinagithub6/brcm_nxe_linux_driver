import yaml
import subprocess
import os
import argparse
import threading
from datetime import datetime
from util import exec_cmd, clone_repo

current_path=os.getcwd()
tool_location = os.getcwd()

with open("brcm_nxe_opt_new.yaml") as stream:
    try:
        brcm_nxe_opt = yaml.safe_load(stream)
        print(brcm_nxe_opt)
    except yaml.YAMLError as exc:
        print(exc)

def get_yaml():
    with open(tool_location + "//brcm_nxe_opt_new.yaml") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def clear_git_vmware_driver_folder(repo_name):
    current_path = os.getcwd()
    vmware_driver_folder = os.listdir(current_path)

    for x in vmware_driver_folder:
        if (x.startswith("vSphere") and os.path.isdir(current_path + "//" + x)):
            del_path = current_path + "//" + x
            command = ["rm", del_path + "//" + "*.zip"]
            exec_cmd(command)
            
def git_commit(src_path, target_branch):
    command = ["git", "add", "."]
    exec_cmd(command)

    command = ["git", "commit", "-m", "test for vmware " + src_path]
    exec_cmd(command)

    # git push --set-upstream origin test_commit_Nov
    command = ["git", "push", "--set-upstream", "origin", target_branch]
    exec_cmd(command)


def do_VMware_Drivers_NXE(drop_location, baseline_branch, new_branch):

    for y in brcm_nxe_opt:
        if "Broadcom-Optimized-VMware_Drivers_NXE" in y["type"]:
            clone_repo(y["git"], None, baseline_branch, new_branch, y["type"])
            now = datetime.now()
            print("before do_VMware_Drivers_NXE")
            print(now)
            clear_git_vmware_driver_folder(y["type"])

    # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle
    path = drop_location + "//drivers_vmware//bundle"
    vmware_distro1 = os.listdir(path)
    for x in vmware_distro1:
        src_vmware_driver_path = path + "//" + x + "//signed"
        # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle\async_80_bundle\signed
        vmware_package_zip = os.listdir(src_vmware_driver_path)
        for package in vmware_package_zip:
            if (len(vmware_package_zip) == 1):
                cmd = 'mkdir ' + src_vmware_driver_path + "//" + package.replace(".zip", "")
                cmd = '7z x ' + src_vmware_driver_path + "//" + package + ' -y -o' + src_vmware_driver_path + "//" + package.replace(".zip", "")
                os.system(cmd)
            # # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle\async_80_bundle\signed
            split_folder_name = x.split("_")
            target_folder_name = "vSphere" + str(float(split_folder_name[1])/10)
            # repo_path = os.path.abspath('../')
            current_path = os.getcwd()
            repository_path = current_path  + "//" + target_folder_name
        
        vendor_src = src_vmware_driver_path + "//" + package.replace(".zip", "") + "//" + package.replace("-package", "")
        repo_dest = repository_path
        command = ["cp", vendor_src, repo_dest]
        exec_cmd(command)

    now = datetime.now()
    print("before do_VMware_Drivers_NXE git commit")
    print(now)
    git_commit(path, new_branch)