import yaml
import subprocess
import os
import argparse
import threading
import re
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit

current_path=os.getcwd()
tool_location = os.getcwd()

def clear_git_fw_pldm_folder(repo_name):
    git_f = current_path + "//" + repo_name
    del_path = git_f + "//" + "images"
    print(del_path)
    command = ["rm", del_path + "//" + "*.pup"]
    exec_cmd(command)

def read_NVM_version(drop_location):
    with open(drop_location + "//" + "release.txt", "r", encoding="utf-8") as f:
        content = f.read()

    nvm_match = re.search(r"NVM Package\s+([\d\.]+)\*", content)
    nvm_version = nvm_match.group(1) if nvm_match else None

    return nvm_version

def do_Firmware_PLDM_NXE(drop_location, baseline_branch, new_branch):
    print('do_Firmware_PLDM_NXE')
    repo_name = "Broadcom-Optimized-Firmware_PLDM_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Optimized-Firmware_PLDM_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_fw_pldm_folder(repo_name)

    #\HPCD_v235.0.4.1\board_sku_files//HPNXESUS_Wh+.pup
    src_vendor_fw_pup_path = drop_location + "//board_sku_files//HPNXESUS_Wh+.pup"
    repository_path = current_path  + "//" + repo_name + "//" + "images"
    command = ["cp", src_vendor_fw_pup_path, repository_path]
    exec_cmd(command)

    filelist = os.listdir(repository_path)
    version_from_release_notes = read_NVM_version(drop_location)
    new_pup_file_name = "bcm" + version_from_release_notes + ".Optimized"
    for file in filelist:
        ori_file = repository_path + "//" + file
        if ".pup.xml" in file:
            print("ori_file")
            print(ori_file)
            print(repository_path + "//" + new_pup_file_name + ".pup.xml")
            os.rename(ori_file, repository_path + "//" + new_pup_file_name + ".pup.xml")
        elif ".pup" in file:
            os.rename(ori_file, repository_path + "//" + new_pup_file_name + ".pup")

    now = datetime.now()
    print("before do_Windows_Drivers_NXE git commit")
    print(now)

    git_commit(src_vendor_fw_pup_path, new_branch)