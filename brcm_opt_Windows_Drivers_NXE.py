import yaml
import subprocess
import os
import argparse
import threading
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit

current_path=os.getcwd()
tool_location = os.getcwd()

def clear_git_win_driver_folder(repo_name):
    git_f = current_path + "//" + repo_name
    g_repo_name = git_f
    # C:\Users\choutin\Documents\GitHub\Windows_Drivers_NXE
    win_driver_folder = os.listdir(git_f)
    print(win_driver_folder)
    for x in win_driver_folder:
        if (os.path.isdir(git_f + "//" + x)) and not x.startswith(".git"):
            del_path = git_f + "//" + x
            print(del_path)
            command = ["rm", del_path + "//" + "*.*"]
            exec_cmd(command)

def do_Windows_Drivers_NXE(drop_location, baseline_branch, new_branch):
    print('do_Windows_Drivers_NXE do_Windows_Drivers_NXE')
    repo_name = "Broadcom-Optimized-Windows_Drivers_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Optimized-Windows_Drivers_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_win_driver_folder(repo_name)

    # path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_windows//bnxtnd//signed"
    path = drop_location + "//drivers_windows//bnxtnd//signed"
    win_distro1 = os.listdir(path)
    print(win_distro1)
    for x in win_distro1:
        if x.startswith("release_2"):
            src_win_driver_path = path + "//" + x
            target_win_driver_folder_name = x.replace('release_', 'win')
            repository_path = current_path  + "//" + repo_name + "//" + target_win_driver_folder_name
            
            command = ["cp", src_win_driver_path + "//" + "*.*", repository_path]
            exec_cmd(command)   

    now = datetime.now()
    print("before do_Windows_Drivers_NXE git commit")
    print(now)

    git_commit(path, new_branch)