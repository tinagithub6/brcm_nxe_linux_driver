import yaml
import subprocess
import os
import argparse
import threading
import re
import json
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit

current_path=os.getcwd()
tool_location = os.getcwd()

def clear_git_fw_folder(repo_name):
    git_f = current_path + "//" + repo_name
    del_path = git_f + "//" + "NVM"
    print(del_path)
    command = ["rm", del_path + "//" + "*.pkg"]
    exec_cmd(command)

def read_version(drop_location):
    with open(drop_location + "//" + "release.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    products = {}

    for line in lines:
        match = re.match(r"^(.*?)\s{2,}(\S+)", line)
        if match and not line.strip().startswith("Product") and not line.strip().startswith("****"):
            product = match.group(1).strip()
            version = match.group(2).strip().rstrip('*')  # 移除星號
            if re.search(r"\d", version):
                products[product] = version

    return products

def modify_json(drop_location, repo_location):
    version_list = read_version(drop_location)
    jsonFile = open(repo_location + "//firmware.json","w")
    data = {
        "Firmware": [
            {
                "Chipset": "NXE",
                "ComboVersion": version_list["NVM Package"],
                "SubFwVers": {
                    "Boot Code": version_list["BootCode(Wh+)"],
                    "NCSI": version_list["APE (NCSI )"],
                    "PXE": version_list["MBA Driver"],
                    "UEFI": version_list["UEFI UNDI"],
                    "CCM": "",
                    "RoCE": version_list["Bono (RoCE)"]
                }
            }
        ]
    }
    json.dump(data, jsonFile)

def do_Firmware_NXE(drop_location, baseline_branch, new_branch):
    print('do_Firmware_NXE')
    repo_name = "Broadcom-Optimized-Firmware_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Optimized-Firmware_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_fw_folder(repo_name)

    #\HPCD_v235.0.4.1\board_sku_files//HPNXESUS_Wh+.pup
    src_vendor_fw_pkg_path = drop_location + "//board_sku_files"
    repository_path = current_path  + "//" + repo_name + "//" + "NVM"
    vendor_pkg_list = os.listdir(src_vendor_fw_pkg_path)
    for pkg in vendor_pkg_list:
        if not pkg.startswith("BCM") and ".pkg" in pkg:
            command = ["cp", src_vendor_fw_pkg_path + "//" + pkg, repository_path]
            exec_cmd(command)

    modify_json(drop_location, repository_path)
    
    # src: C:\Users\choutin\Downloads\HPCD_v235.0.4.1\utils\hpfwupglib\windows
    # dest: C:\Users\choutin\Documents\project\commit_tool_test\Broadcom-Optimized-Firmware_NXE\libs\Windows\x86_64
    src_vendor_win_fw_lib_path = drop_location + "//utils//hpfwupglib//windows//*.dll"
    repository_path = current_path  + "//" + repo_name + "//libs//Windows//x86_64"
    command = ["cp", src_vendor_win_fw_lib_path, repository_path]
    exec_cmd(command)

    # src: C:\Users\choutin\Downloads\HPCD_v235.0.4.1\utils\hpfwupglib\esxi7
    # dest: C:\Users\choutin\Documents\project\commit_tool_test\Broadcom-Optimized-Firmware_NXE\libs\VMware
    src_vendor_vmware_fw_lib_path = drop_location + "//utils//hpfwupglib//esxi7//libbrcm_hpfwupg.so"
    repository_path = current_path  + "//" + repo_name + "//libs//VMware"
    dest_vmwaer_folderlist = os.listdir(repository_path)
    for folder in dest_vmwaer_folderlist:
        #     ori_file = repository_path + "//" + file
        command = ["cp", src_vendor_vmware_fw_lib_path, repository_path + "//" + folder]
        exec_cmd(command)

    # src C:\Users\choutin\Downloads\HPCD_v235.0.4.1\utils\hpfwupglib\linux_x86_64
    # dest: C:\Users\choutin\Documents\project\commit_tool_test\Broadcom-Optimized-Firmware_NXE\libs\Linux\x86_64\libs
    src_vendor_linux_fw_lib_path = drop_location + "//utils//hpfwupglib//linux_x86_64//libbrcm_hpfwupg.so"
    repository_path = current_path  + "//" + repo_name + "//libs//Linux//x86_64//libs"
    command = ["cp", src_vendor_linux_fw_lib_path, repository_path]
    exec_cmd(command)

    git_commit(src_vendor_fw_pkg_path, new_branch)