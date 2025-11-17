import os
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit, clear_git_fw_folder, modify_json

current_path=os.getcwd()
tool_location = os.getcwd()

def do_open_Firmware_NXE(drop_location, baseline_branch, new_branch):
    print('do_open_Firmware_NXE')
    repo_name = "Broadcom-Open-Firmware_Open_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Open-Firmware_Open_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_fw_folder(repo_name)

    # src: \HPBCMCD_v235.0.4.1\board_sku_files
    # dest: Broadcom-Open-Firmware_Open_NXE/NVM
    src_vendor_fw_pkg_path = drop_location + "//board_sku_files"
    repository_path = current_path  + "//" + repo_name + "//" + "NVM"
    brcm_open_adapter = ["57412", "57414", "57416", "57504"]
    vendor_pkg_list = os.listdir(src_vendor_fw_pkg_path)
    for pkg in vendor_pkg_list:
        if pkg.startswith("BCM") and ".pkg" in pkg and pkg[4:9] in brcm_open_adapter:
            command = ["cp", src_vendor_fw_pkg_path + "//" + pkg, repository_path]
            exec_cmd(command)

    modify_json(drop_location, repository_path)
    
    # src: HPBCMCD_v235.0.4.1\utils\hpfwupglib\windows
    # dest: Broadcom-Open-Firmware_Open_NXE/libs/Windows/x86_64/
    src_vendor_win_fw_lib_path = drop_location + "//utils//hpfwupglib//windows//*.dll"
    repository_path = current_path  + "//" + repo_name + "//libs//Windows//x86_64"
    command = ["cp", src_vendor_win_fw_lib_path, repository_path]
    exec_cmd(command)

    # src: HPBCMCD_v235.0.4.1\utils\hpfwupglib\esxi7
    # dest: Broadcom-Open-Firmware_Open_NXE/libs/VMware/
    src_vendor_vmware_fw_lib_path = drop_location + "//utils//hpfwupglib//esxi7//libbrcm_hpfwupg.so"
    repository_path = current_path  + "//" + repo_name + "//libs//VMware"
    dest_vmwaer_folderlist = os.listdir(repository_path)
    for folder in dest_vmwaer_folderlist:
        command = ["cp", src_vendor_vmware_fw_lib_path, repository_path + "//" + folder]
        exec_cmd(command)

    # src: HPBCMCD_v235.0.4.1\utils\hpfwupglib\linux_x86_64
    # dest: Broadcom-Open-Firmware_Open_NXE\libs\Linux\x86_64\libs
    src_vendor_linux_fw_lib_path = drop_location + "//utils//hpfwupglib//linux_x86_64//libbrcm_hpfwupg.so"
    repository_path = current_path  + "//" + repo_name + "//libs//Linux//x86_64//libs"
    command = ["cp", src_vendor_linux_fw_lib_path, repository_path]
    exec_cmd(command)

    git_commit(src_vendor_fw_pkg_path, new_branch)