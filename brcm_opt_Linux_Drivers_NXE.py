import yaml
import subprocess
import os
import argparse
import threading
from datetime import datetime
from util import exec_cmd, clone_repo

current_path=os.getcwd()
tool_location = os.getcwd()

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

def clear_git_kmps_folder(repo_name):
    src_git_folder = current_path + "//" + repo_name + "//kmps"
    kmps_folder = os.listdir(src_git_folder)
    print(kmps_folder)
    for x in kmps_folder:
        if (os.path.isdir(src_git_folder + "//" + x)):
            src_git_del_path = src_git_folder + "//" + x + "//" + "x86_64"
            command = ["rm", src_git_del_path + "//" + "*.rpm"]
            exec_cmd(command)

def clear_git_libbnxtre_folder(repo_name):
    src_git_folder = current_path + "//" + repo_name + "//" + "libbnxtre"
    # 'C://Users//choutin//Documents//Linux_Drivers_NXE//libbnxtre'
    kmps_folder = os.listdir(src_git_folder)
    for x in kmps_folder:
        if (os.path.isdir(src_git_folder + "//" + x)):
            distro = os.listdir(src_git_folder + "//" + x)
            for y in distro:
                if (os.path.isdir(src_git_folder + "//" + x + "//"+ y)):
                    del_path = src_git_folder + "//" + x + "//" + y + "//" + "x86_64"
                    command = ["rm", del_path + "//" + "*.rpm"]
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


def do_Linux_Drivers_NXE(drop_location, baseline_branch, new_branch):
    brcm_nxe_opt=get_yaml()
    repository_path = ""
    Linux_Drivers_NXE_linux_os = ['rhel', 'suse']
    for y in brcm_nxe_opt:
        print(y)
        print(y["type"])
        if "Broadcom-Optimized-Linux_Drivers_NXE" in y["type"]:
            repository_path = current_path + "//" + y["type"]
            Linux_Drivers_NXE_linux_folder_prefix = y["folder_prefix"]
            clone_repo(y["git"], None, baseline_branch, new_branch, y["type"])
            now = datetime.now()
            print("before do_Linux_Drivers_NXE")
            print(now)
            clear_git_kmps_folder(y["type"])
            clear_git_libbnxtre_folder(y["type"])

    for linux_type in Linux_Drivers_NXE_linux_folder_prefix:
        dest_roce_path = os.listdir(drop_location + "//drivers_linux//bnxt_rocelib//rpm" + "//"  + linux_type)
        print(dest_roce_path)
        for x in dest_roce_path:
            drop_path = drop_location + "//drivers_linux//bnxt_rocelib//rpm" + "//" + linux_type + "//" + x
            linux_distro1 = os.listdir(drop_path)
            for y in linux_distro1:
                substrings_to_avoid = ["debug", "devel", "src"]
                if (y.startswith("libbnxt_re-") and all(sub not in y for sub in substrings_to_avoid)):
                    directory_path = repository_path + "//" + "libbnxtre" + "//" + x.partition('.')[0]
                    if os.path.isdir(directory_path):
                        print(f"The directory under bnxt_rocelib rpm '{directory_path}' exists.")
                        dest_libbnxtre_path = repository_path + "//" + "libbnxtre"
                        dest_libbnxtre_distro_path = dest_libbnxtre_path + "//" + x.partition('.')[0]
                        lib_folder_name = ''
                        if linux_type == 'rhel':
                            lib_folder_name = x.replace('.', 'u')
                        elif linux_type == 'suse':
                            lib_folder_name = x.replace('.', 'sp')

                        dest_full_path = dest_libbnxtre_distro_path + "//" + lib_folder_name

                        if not os.path.isdir(dest_full_path):
                            command = ["mkdir", dest_full_path]
                            exec_cmd(command)

                            command = ["mkdir", dest_full_path + "//" + "x86_64"]
                            exec_cmd(command)
                    else:
                        print(f"The directory under bnxt_rocelib rpm '{directory_path}' does not exist.")
                        dest_libbnxtre_path = repository_path + "//" + "libbnxtre"
                        # os.chdir(dest_libbnxtre_path)
                        
                        # command = ["mkdir", x.partition('.')[0]]
                        command = ["mkdir", dest_libbnxtre_path + "//" + x.partition('.')[0]]
                        exec_cmd(command)

                        dest_libbnxtre_distro_path = dest_libbnxtre_path + "//" + x.partition('.')[0]
                        # os.chdir(dest_libbnxtre_distro_path) #pair 1
                        if linux_type == 'rhel':
                            lib_folder_name = x.replace('.', 'u')
                        elif linux_type == 'suse':
                            lib_folder_name = x.replace('.', 'sp')
                        # command = ["mkdir", lib_folder_name] #pair 1
                        command = ["mkdir", dest_libbnxtre_distro_path + "//" + lib_folder_name]
                        exec_cmd(command)
                        
                        dest_full_path = dest_libbnxtre_distro_path + "//" + lib_folder_name
                        # os.chdir(dest_full_path)
                        # command = ["mkdir", "x86_64"]
                        command = ["mkdir", dest_full_path + "//" + "x86_64"]
                        exec_cmd(command)
    
                    target_path = dest_full_path + "//" + "x86_64"
                    src_path = drop_path + "//" + y

                    command = ["cp", src_path, target_path]
                    exec_cmd(command)

        src_kmp_path = os.listdir(drop_location +'//drivers_linux//bundle//kmp//' + linux_type)
        print(src_kmp_path)
        for x in src_kmp_path:
            drop_path = drop_location + "//drivers_linux//bundle//kmp//" + linux_type + "//" + x
            linux_distro1 = os.listdir(drop_path)
            for y in linux_distro1:
                if (linux_type == 'rhel' and y.startswith("kmod-bnxt_en") and "debuginfo" not in y) \
                    or (linux_type == 'suse' and y.startswith("bnxt_en-kmp-default") and \
                    "debuginfo" not in y):

                    directory_path = repository_path + "//" + "kmps" + "//" + x.partition('.')[0]
                    # print("linux component:")
                    # print("bnxt." + x.partition('.')[0])
                    # componentlist.add("bnxt." + x.partition('.')[0])
                    # with open("C://Users//choutin//Documents//project//brcm_nxe_linux_driver//my_file.txt", "a") as file:
                    #     # Write the new content to the file
                    #     file.write("bnxt." + x.partition('.')[0])
                    #     file.write("\n")
                    if not os.path.isdir(directory_path):
                        print(f"The directory '{directory_path}' does not exist.")
                        dest_kmp_path = repository_path + "//" + "kmps"
                        # os.chdir(dest_kmp_path)
                        
                        command = ["mkdir", dest_kmp_path + "//" + x.partition('.')[0]]
                        exec_cmd(command)

                        # os.chdir(directory_path)
                        command = ["mkdir", dest_kmp_path + "//" + x.partition('.')[0] + "//" + "x86_64"]
                        exec_cmd(command)
                    
                    target_path = repository_path + "//" + "kmps" + "//" + x.partition('.')[0] + "//" + "x86_64"
                    print(target_path)
                    src_path = drop_path + "//" + y
                    print(src_path)

                    command = ["cp", src_path, target_path]
                    exec_cmd(command)            

    now = datetime.now()
    print("before do_Linux_Drivers_NXE git commit")
    print(now)
    # git_commit(src_path, new_branch)