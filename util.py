import yaml
import subprocess
import os
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

# def get_yaml():
#     # with open("brcm_nxe_opt.yaml") as stream:
#     with open("C://users//choutin//Documents//project//brcm_nxe_linux_driver//brcm_nxe_opt_new1212.yaml") as stream:
#         try:
#             return yaml.safe_load(stream)
#             # print(yaml.safe_load(stream))
#             # brcm_nxe_opt = yaml.safe_load(stream)
#             # print(brcm_nxe_opt)
#         except yaml.YAMLError as exc:
#             print(exc)
