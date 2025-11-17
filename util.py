import subprocess
import os
import json
import re
from datetime import datetime

current_path = os.getcwd()
tool_path = os.getcwd()

def exec_cmd(command):
    print(f"exec_cmd")
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"'{command}' exec successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error exec_cmd: {e}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("FileNotFoundError: exec_cmd.")

def clone_repo(repo_url, target_directory=None, src_branch=None, target_branch=None, repo_name=None):
    """
    Clones a Git repository.

    Args:
        repo_url (str): The URL of the Git repository to clone.
        target_directory (str, optional): The directory where the repository
                                          should be cloned. If None, Git will
                                          create a directory named after the
                                          repository.
    """
    print("clone_repo clone_repo")
    command = ["git", "clone", "https://github.hpe.com/hpe/" + repo_name + ".git"]
    if target_directory:
        command.append(target_directory)
    exec_cmd(command)
    
    os.chdir(tool_path + "//" + repo_name)
    if (src_branch == target_branch):
        command = ["git", "switch", target_branch]
        exec_cmd(command)

        command = ["git", "pull"]
        exec_cmd(command)
    else:
        command = ["git", "switch", src_branch]
        exec_cmd(command)

        command = ["git", "checkout", "--orphan", target_branch]
        exec_cmd(command)

def git_commit(src_path, target_branch):
    # command = ["git", "commit", "-A", "-m", "test" + src_path]
    command = ["git", "add", "."]
    exec_cmd(command)

    command = ["git", "commit", "-m", src_path]
    exec_cmd(command)

    # git push --set-upstream origin test_commit_Nov
    command = ["git", "push", "--set-upstream", "origin", target_branch]
    exec_cmd(command)


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

def clear_git_win_driver_folder(repo_name):
    git_f = current_path + "//" + repo_name
    win_driver_folder = os.listdir(git_f)
    print(win_driver_folder)
    for x in win_driver_folder:
        if (os.path.isdir(git_f + "//" + x)) and not x.startswith(".git"):
            del_path = git_f + "//" + x
            print(del_path)
            command = ["rm", del_path + "//" + "*.*"]
            exec_cmd(command)
