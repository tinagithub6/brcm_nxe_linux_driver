import yaml
import subprocess
import os
import argparse
import threading
import re
from datetime import datetime
from util import exec_cmd, clone_repo

current_path=os.getcwd()
tool_location = os.getcwd()
g_repo_name = ""
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

def clear_git_fw_pldm_folder(repo_name):
    git_f = current_path + "//" + repo_name
    del_path = git_f + "//" + "images"
    print(del_path)
    command = ["rm", del_path + "//" + "*.pup"]
    exec_cmd(command)

    #bcm235.1.160000.Optimized.pup
    #bcm235.1.160000.Optimized.pup.xml
def git_commit(src_path, target_branch):
    # 先拉取遠端更新再推送（推薦）
    # --rebase 會把你的本地提交移到遠端最新提交之後，保持乾淨的歷史。
    # git pull --rebase origin test_NXE_pldm



    command = ["git", "add", "."]
    exec_cmd(command)

    command = ["git", "commit", "-m", "test for FW PLDM " + src_path]
    exec_cmd(command)

    # command = ["git", "pull", "--rebase", "origin", target_branch]
    # exec_cmd(command)

    # git push --set-upstream origin test_commit_Nov
    command = ["git", "push", "--set-upstream", "origin", target_branch]
    exec_cmd(command)

def read_NVM_version(drop_location):
    with open(drop_location + "//" + "release.txt", "r", encoding="utf-8") as f:
        content = f.read()

    nvm_match = re.search(r"NVM Package\s+([\d\.]+)\*", content)
    nvm_version = nvm_match.group(1) if nvm_match else None

    return nvm_version

def do_Firmware_PLDM_NXE(drop_location, baseline_branch, new_branch):
    print('do_Firmware_PLDM_NXE')
    brcm_nxe_opt=get_yaml()
    repo_name = ''
    for y in brcm_nxe_opt:
        if "Broadcom-Optimized-Firmware_PLDM_NXE" in y["type"]:
    #             try:
    #     subprocess.run(command, check=True, capture_output=True, text=True)
    #     print(f"'{command}' exec successfully.")
    # except subprocess.CalledProcessError as e:
            try:
                clone_repo(y["git"], None, baseline_branch, new_branch, y["type"])
            except subprocess.CalledProcessError as e:
                print("pldm clone error")
                print(f"pldm clone error Error exec_cmd: {e}")
                print(f"pldm clone error Stderr: {e.stderr}")
                # git pull --rebase origin test_NXE_pldm
            repo_name = y["type"]
            # now = datetime.now()
            # print("before do_Windows_Drivers_NXE")
            # print(now)
            clear_git_fw_pldm_folder(y["type"])

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