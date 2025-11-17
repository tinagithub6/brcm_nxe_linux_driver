import os
import re
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit

current_path=os.getcwd()
tool_location = os.getcwd()

def clear_git_fw_pldm_folder(repo_name):
    git_f = current_path + "//" + repo_name
    del_path = git_f + "//" + "images"
    folderlist = os.listdir(del_path)
    for sub_folder in folderlist:
        print(sub_folder)
        print(del_path + "//" + sub_folder)
        command = ["rm", del_path + "//" + sub_folder + "//" + "*.pup"]
        exec_cmd(command)

def read_NVM_version(drop_location):
    with open(drop_location + "//" + "release.txt", "r", encoding="utf-8") as f:
        content = f.read()

    nvm_match = re.search(r"NVM Package\s+([\d\.]+)\*", content)
    nvm_version = nvm_match.group(1) if nvm_match else None

    return nvm_version

def rename_pup_xml(drop_location, repository_path, suffix):
    filelist = os.listdir(repository_path)
    version_from_release_notes = read_NVM_version(drop_location)
    new_pup_file_name = "bcm" + version_from_release_notes
    for file in filelist:
        ori_file = repository_path + "//" + file
        if ".pup.xml" in file:
            os.rename(ori_file, repository_path + "//" + new_pup_file_name + suffix + ".pup.xml")
        elif ".pup" in file:
            os.rename(ori_file, repository_path + "//" + new_pup_file_name + suffix + ".pup")

def do_open_Firmware_PLDM_NXE(drop_location, baseline_branch, new_branch):
    print('do_open_Firmware_PLDM_NXE')
    repo_name = "Broadcom-Open-Firmware_PLDM_Open_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Open-Firmware_PLDM_Open_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_fw_pldm_folder(repo_name)

    #src: C:\Users\choutin\Downloads\HPBCMCD_v235.0.4.2\board_sku_files\HPNXEOPEN_Wh+.pup
    #dest: Broadcom-Open-Firmware_PLDM_Open_NXE/images/5741x/bcm235.1.160.0.pup
    src_vendor_fw_pup_path = drop_location + "//board_sku_files//HPNXEOPEN_Wh+.pup"
    repository_path = current_path  + "//" + repo_name + "//" + "images" + "//" + "5741x"
    command = ["cp", src_vendor_fw_pup_path, repository_path]
    exec_cmd(command)

    rename_pup_xml(drop_location, repository_path, "")

    src_vendor_fw_pup_path = drop_location + "//board_sku_files//HPNXEOPEN_Thor.pup"
    repository_path = current_path  + "//" + repo_name + "//" + "images" + "//" + "5750x"
    command = ["cp", src_vendor_fw_pup_path, repository_path]
    exec_cmd(command)

    rename_pup_xml(drop_location, repository_path, "_Thor")

    src_vendor_fw_pup_path = drop_location + "//board_sku_files//HPNXEOPEN_Thor2.pup"
    repository_path = current_path  + "//" + repo_name + "//" + "images" + "//" + "5760x"
    command = ["cp", src_vendor_fw_pup_path, repository_path]
    exec_cmd(command)

    rename_pup_xml(drop_location, repository_path, "_Thor2")

    src_vendor_fw_pup_path = drop_location + "//board_sku_files//BCM957608-N2100HQI00.pup"
    repository_path = current_path  + "//" + repo_name + "//" + "images" + "//" + "957608_N2100HQI00"
    command = ["cp", src_vendor_fw_pup_path, repository_path]
    exec_cmd(command)

    rename_pup_xml(drop_location, repository_path, "_BCM957608-N2100HQI00")

    src_vendor_fw_pup_path = drop_location + "//board_sku_files//BCM957608-P2100HQF00.pup"
    repository_path = current_path  + "//" + repo_name + "//" + "images" + "//" + "957608_P2100HQF00"
    command = ["cp", src_vendor_fw_pup_path, repository_path]
    exec_cmd(command)

    rename_pup_xml(drop_location, repository_path, "_BCM957608-P2100HQF00")

    git_commit(src_vendor_fw_pup_path, new_branch)