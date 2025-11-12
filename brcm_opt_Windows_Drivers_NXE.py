import yaml
import subprocess
import os
import argparse
import threading
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

def clear_git_win_driver_folder(repo_name):
    git_f = current_path + "//" + repo_name
    g_repo_name = git_f
    # C:\Users\choutin\Documents\GitHub\Windows_Drivers_NXE
    win_driver_folder = os.listdir(git_f)
    print(win_driver_folder)
    for x in win_driver_folder:
        if (os.path.isdir(git_f + "//" + x)):
            del_path = git_f + "//" + x
            print(del_path)
            # os.chdir(del_path)
            # command = ["rm", "*.*"]
            command = ["rm", del_path + "//" + "*.*"]
            exec_cmd(command)
            
def git_commit(src_path, target_branch): #git_commit_opt_win_drv
    print("g_repo_name")
    print(g_repo_name)
    tmp = os.getcwd()
    print("getcwd")
    print(tmp)
    # command = ["git", "commit", "-A", "-m", "test" + src_path]
    command = ["git", "add", "."]
    exec_cmd(command)

    command = ["git", "commit", "-m", "test for windows " + src_path]
    exec_cmd(command)

    # git push --set-upstream origin test_commit_Nov
    command = ["git", "push", "--set-upstream", "origin", target_branch]
    exec_cmd(command)


def do_Windows_Drivers_NXE(drop_location, baseline_branch, new_branch):
    print('do_Windows_Drivers_NXE do_Windows_Drivers_NXE')
    brcm_nxe_opt=get_yaml()
    repo_name = ''
    for y in brcm_nxe_opt:
        if "Broadcom-Optimized-Windows_Drivers_NXE" in y["type"]:
            Windows_Drivers_NXE_win_folder_prefix = y["folder_prefix"]
            clone_repo(y["git"], None, baseline_branch, new_branch, y["type"])
            repo_name = y["type"]
            now = datetime.now()
            print("before do_Windows_Drivers_NXE")
            print(now)
            clear_git_win_driver_folder(y["type"])

    # path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_windows//bnxtnd//signed"
    path = drop_location + "//drivers_windows//bnxtnd//signed"
    win_distro1 = os.listdir(path)
    print(win_distro1)
    # componentlistw=set()
    for x in win_distro1:
        if x.startswith("release_2"):
            src_win_driver_path = path + "//" + x
            target_win_driver_folder_name = x.replace('release_', 'win')
            repository_path = current_path  + "//" + repo_name + "//" + target_win_driver_folder_name
            print(src_win_driver_path)
            print(repository_path)
            
            # print("bnxtnd."+target_win_driver_folder_name.replace('win', "w").replace('0', "k"))
            # componentlistw.add("bnxtnd."+target_win_driver_folder_name.replace('win', "w").replace('0', "k"))
            # print("component:")
            # print(componentlistw)
            command = ["cp", src_win_driver_path + "//" + "*.*", repository_path]
            exec_cmd(command)   

    now = datetime.now()
    print("before do_Windows_Drivers_NXE git commit")
    print(now)

    # git_commit(path, new_branch)