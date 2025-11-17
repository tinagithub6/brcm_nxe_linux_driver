import os
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit, clear_git_win_driver_folder

current_path=os.getcwd()
tool_location = os.getcwd()

def do_open_Windows_Drivers_NXE(drop_location, baseline_branch, new_branch):
    print('do_Windows_Drivers_NXE do_Windows_Drivers_NXE')
    repo_name = "Broadcom-Open-Windows_Drivers_Open_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Open-Windows_Drivers_Open_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_win_driver_folder(repo_name)

    # src: C:\Users\choutin\Downloads\HPBCMCD_v235.0.4.2\drivers_windows\bnxtnd\signed
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