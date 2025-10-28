import yaml
import subprocess
import os

current_path = os.getcwd()

brcm_nxe_opt = ""
repository_path = current_path + "//" + "Linux_Drivers_NXE"
# "C://Users//choutin//Documents//Linux_Drivers_NXE"

NXE_OPT = 'HPCD_v235.0.4.1'
os.system('7z x C://Users//choutin//Downloads//' + NXE_OPT + ".zip" ' -y -oC://Users//choutin//Downloads//' + NXE_OPT)

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

def clone_repo(repo_url, target_directory=None, src_branch=None, target_branch=None):
    """
    Clones a Git repository.

    Args:
        repo_url (str): The URL of the Git repository to clone.
        target_directory (str, optional): The directory where the repository
                                          should be cloned. If None, Git will
                                          create a directory named after the
                                          repository.
    """
    command = ["git", "clone", repo_url]
    if target_directory:
        command.append(target_directory)

    exec_cmd(command)

    # NovSPP2025_Gen10Gen11Gen12
    # git checkout --orphan Gen10PlusGen11March2024_CVL
    
    repository_path = current_path + "//Linux_Drivers_NXE"
    # "C://Users//choutin//Documents//Linux_Drivers_NXE"
    os.chdir(repository_path)

    command = ["git", "switch", src_branch]
    exec_cmd(command)

    command = ["git", "checkout", "--orphan", target_branch]
    exec_cmd(command)

def clear_git_kmps_folder():
    git_f = current_path + "//Linux_Drivers_NXE//kmps"
    # 'C://Users//choutin//Documents//Linux_Drivers_NXE//kmps'
    kmps_folder = os.listdir(git_f)
    print(kmps_folder)
    for x in kmps_folder:
        if (os.path.isdir(git_f + "//" + x)):
            del_path = git_f + "//" + x + "//" + "x86_64"
            print(del_path)
            os.chdir(del_path)
            command = ["rm", "*.rpm"]
            exec_cmd(command)

def clear_git_libbnxtre_folder():
    git_f = current_path + "//Linux_Drivers_NXE//libbnxtre"
    # 'C://Users//choutin//Documents//Linux_Drivers_NXE//libbnxtre'
    kmps_folder = os.listdir(git_f)
    print(kmps_folder)
    for x in kmps_folder:
        if (os.path.isdir(git_f + "//" + x)):
            distro = os.listdir(git_f + "//" + x)
            print("+++++++++++++")
            print(distro)
            for y in distro:
                if (os.path.isdir(git_f + "//" + x + "//"+ y)):
                    del_path = git_f + "//" + x + "//" + y + "//" + "x86_64"
                    print(del_path)
                    os.chdir(del_path)
                    command = ["rm", "*.rpm"]
                    exec_cmd(command)

def copy_to_git_folder(repo_url, target_directory=None, src_branch=None, target_branch=None):
    """
    Clones a Git repository.

    Args:
        repo_url (str): The URL of the Git repository to clone.
        target_directory (str, optional): The directory where the repository
                                          should be cloned. If None, Git will
                                          create a directory named after the
                                          repository.
    """
    command = ["git", "clone", repo_url]
    if target_directory:
        command.append(target_directory)

    exec_cmd(command)
    
    repository_path = current_path + "//Linux_Drivers_NXE"
    # "C://Users//choutin//Documents//Linux_Drivers_NXE"
    os.chdir(repository_path)

    command = ["git", "switch", src_branch]
    exec_cmd(command)


with open("brcm_nxe_opt.yaml") as stream:
    try:
        print(yaml.safe_load(stream))
        brcm_nxe_opt = yaml.safe_load(stream)
        print(brcm_nxe_opt)
    except yaml.YAMLError as exc:
        print(exc)

def get_yaml():
    with open("brcm_nxe_opt.yaml") as stream:
        try:
            return yaml.safe_load(stream)
            # print(yaml.safe_load(stream))
            # brcm_nxe_opt = yaml.safe_load(stream)
            # print(brcm_nxe_opt)
        except yaml.YAMLError as exc:
            print(exc)

brcm_nxe_opt=get_yaml()
# print(brcm_nxe_opt)
for y in brcm_nxe_opt:
    if "HPCD" in y:
        for z in brcm_nxe_opt[y]:
            print(z)
            print(z["folder_prefix"])
            if z["folder_prefix"] == 'rhel':
                repo_to_clone = z["git"]
                clone_repo(repo_to_clone, None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12')
                clear_git_kmps_folder()
                clear_git_libbnxtre_folder()



linux_os = ['rhel', 'suse']
for linux_type in linux_os:
    dest_roce_path = os.listdir('C://Users//choutin//Downloads//' + NXE_OPT + '//drivers_linux//bnxt_rocelib//rpm' + "//"  + linux_type)
    print(dest_roce_path)
    for x in dest_roce_path:
        path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_linux//bnxt_rocelib//rpm" + "//" + linux_type + "//" + x
        linux_distro1 = os.listdir(path)
        for y in linux_distro1:
            substrings_to_avoid = ["debug", "devel", "src"]
            if (y.startswith("libbnxt_re-") and all(sub not in y for sub in substrings_to_avoid)):
                print('===------')
                print(y)
                directory_path = repository_path + "//" + "libbnxtre" + "//" + x.partition('.')[0]
                print(directory_path)
                if os.path.isdir(directory_path):
                    print(f"suse The directory '{directory_path}' exists.")
                    dest_libbnxtre_path = repository_path + "//" + "libbnxtre"
                    dest_libbnxtre_distro_path = dest_libbnxtre_path + "//" + x.partition('.')[0]
                    lib_folder_name = ''
                    if linux_type == 'rhel':
                        lib_folder_name = x.replace('.', 'u')
                    elif linux_type == 'suse':
                        lib_folder_name = x.replace('.', 'sp')

                    dest_full_paths = dest_libbnxtre_distro_path + "//" + lib_folder_name

                    if os.path.isdir(dest_full_paths):
                        print('yesssss')
                    else:
                        print(dest_full_paths)
                        print('noooooo')
                        command = ["mkdir", dest_full_paths]
                        exec_cmd(command)

                        command = ["mkdir", dest_full_paths + "//" + "x86_64"]
                        exec_cmd(command)


                else:
                    print(f"suse The directory '{directory_path}' does not exist.")
                    dest_libbnxtre_path = repository_path + "//" + "libbnxtre"
                    os.chdir(dest_libbnxtre_path)
                    
                    command = ["mkdir", x.partition('.')[0]]
                    exec_cmd(command)

                    dest_libbnxtre_distro_path = dest_libbnxtre_path + "//" + x.partition('.')[0]
                    os.chdir(dest_libbnxtre_distro_path)
                    if linux_type == 'rhel':
                        lib_folder_name = x.replace('.', 'u')
                    elif linux_type == 'suse':
                        lib_folder_name = x.replace('.', 'sp')
                    command = ["mkdir", lib_folder_name]
                    exec_cmd(command)
                    
                    dest_full_path = dest_libbnxtre_distro_path + "//" + lib_folder_name
                    os.chdir(dest_full_path)
                    command = ["mkdir", "x86_64"]
                    exec_cmd(command)
 
                target_path = dest_full_path + "//" + "x86_64"
                print(target_path)
                src_path = path + "//" + y
                print(src_path)

                print("cp 451")
                command = ["cp", src_path, target_path]
                exec_cmd(command)
                # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]


# linux_os = ['rhel', 'suse']
# for linux_type in linux_os:
    src_kmp_path = os.listdir('C://Users//choutin//Downloads//' + NXE_OPT +'//drivers_linux//bundle//kmp//' + linux_type)
    print(src_kmp_path)
    for x in src_kmp_path:
        path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_linux//bundle//kmp//" + linux_type + "//" + x
        linux_distro1 = os.listdir(path)
        print('------')
        print(linux_distro1)
        for y in linux_distro1:
            # path = "C://Users//choutin//Downloads//HPCD_v235.0.1.1//drivers_linux//bundle//kmp//rhel" + "//" + x + "//" + y
            # print(y)
            if (linux_type == 'rhel' and y.startswith("kmod-bnxt_en") and "debuginfo" not in y) \
                or (linux_type == 'suse' and y.startswith("bnxt_en-kmp-default") and \
                "debuginfo" not in y):
                print(y)
                # copy_to_git_folder(y) "C://Users//choutin//Documents//Linux_Drivers_NXE"
                
                directory_path = repository_path + "//" + "kmps" + "//" + x.partition('.')[0]
                if os.path.isdir(directory_path):
                    print(f"The directory '{directory_path}' exists.")
                else:
                    print(f"The directory '{directory_path}' does not exist.")
                    dest_kmp_path = repository_path + "//" + "kmps"
                    os.chdir(dest_kmp_path)
                    
                    command = ["mkdir", x.partition('.')[0]]
                    exec_cmd(command)

                    os.chdir(directory_path)
                    command = ["mkdir", "x86_64"]
                    exec_cmd(command)
                
                target_path = repository_path + "//" + "kmps" + "//" + x.partition('.')[0] + "//" + "x86_64"
                print(target_path)
                src_path = path + "//" + y
                print(src_path)

                command = ["cp", src_path, target_path]
                exec_cmd(command)

# target_path = repository_path
# print(target_path)
# # print(os.chdir(target_path))
# os.chdir(target_path)
# print(current_path + "//" + "git_change.txt")
# command = ["git", "status", ">>", target_path + "//" + "git_change.txt"]
# exec_cmd(command)

# import os

# def delete_rpm_files(folder_path):
#     """
#     刪除指定資料夾及其所有子資料夾中的 .rpm 檔案

#     :param folder_path: 要處理的根資料夾路徑
#     """
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith('.rpm'):
#                 file_path = os.path.join(root, file)
#                 try:
#                     os.remove(file_path)
#                     print(f"Deleted: {file_path}")
#                 except Exception as e:
#                     print(f"Failed to delete {file_path}: {e}")

# 使用範例
# delete_rpm_files("/path/to/your/folder")