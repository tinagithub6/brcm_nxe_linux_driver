import yaml
import subprocess
import os
import argparse
import threading
from datetime import datetime
from brcm_opt_VMware_Drivers_NXE import do_VMware_Drivers_NXE

parser = argparse.ArgumentParser(description="A simple greeting script.")
parser.add_argument("baseline_branch", type=str, help="The name of the person to greet.")
parser.add_argument("new_branch", type=str, help="The age of the person.")
componentlist = set()

args = parser.parse_args()

print(f"Hello, {args.baseline_branch}! You are {args.new_branch} years old.")
# MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12

# exit
current_path = os.getcwd()

brcm_nxe_opt = ""
repository_path = current_path + "//" + "Linux_Drivers_NXE"
# "C://Users//choutin//Documents//Linux_Drivers_NXE"

NXE_OPT = 'HPCD_v235.0.4.1'
now = datetime.now()
print("before 7z start")
print(now)
# os.system('7z x C://Users//choutin//Downloads//' + NXE_OPT + ".zip" ' -y -oC://Users//choutin//Downloads//' + NXE_OPT)
end = datetime.now()
print("before 7z finished")
print(end)

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
    command = ["git", "clone", repo_url]
    if target_directory:
        command.append(target_directory)

    exec_cmd(command)

    # NovSPP2025_Gen10Gen11Gen12
    # git checkout --orphan Gen10PlusGen11March2024_CVL
    
    repository_path = current_path + "//" + repo_name
    # "C://Users//choutin//Documents//Linux_Drivers_NXE"
    os.chdir(repository_path)

    if (args.baseline_branch == args.new_branch):
        command = ["git", "switch", args.new_branch]
        exec_cmd(command)

        command = ["git", "pull"]
        exec_cmd(command)
    else:
        command = ["git", "switch", args.baseline_branch]
        exec_cmd(command)

        command = ["git", "checkout", "--orphan", target_branch]
        exec_cmd(command)

def clear_git_win_driver_folder(repo_name):
    git_f = current_path + "//" + repo_name
    # C:\Users\choutin\Documents\GitHub\Windows_Drivers_NXE
    win_driver_folder = os.listdir(git_f)
    print(win_driver_folder)
    for x in win_driver_folder:
        if (os.path.isdir(git_f + "//" + x)):
            del_path = git_f + "//" + x
            print(del_path)
            os.chdir(del_path)
            command = ["rm", "*.*"]
            exec_cmd(command)

def clear_git_kmps_folder(repo_name):
    # git_f = current_path + "//Linux_Drivers_NXE//kmps"
    git_f = current_path + "//" + repo_name + "//kmps"
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


# with open("brcm_nxe_opt.yaml") as stream:
with open("brcm_nxe_opt_new.yaml") as stream:
    try:
        print("global 111")
        # print(yaml.safe_load(stream))
        brcm_nxe_opt = yaml.safe_load(stream)
        print(brcm_nxe_opt)
    except yaml.YAMLError as exc:
        print(exc)

def get_yaml():
    # with open("brcm_nxe_opt.yaml") as stream:
    with open("C://users//choutin//Documents//project//brcm_nxe_linux_driver//brcm_nxe_opt_new1212.yaml") as stream:
        try:
            return yaml.safe_load(stream)
            # print(yaml.safe_load(stream))
            # brcm_nxe_opt = yaml.safe_load(stream)
            # print(brcm_nxe_opt)
        except yaml.YAMLError as exc:
            print(exc)

# def do_VMware_Drivers_NXE():
#     print('do_VMware_Drivers_NXE do_VMware_Drivers_NXE')
#     # brcm_nxe_opt=get_yaml()
#     # print("ignore get_yaml")
#     repo_name = ''
#     for y in brcm_nxe_opt:
#         if "VMware_Drivers_NXE" in y["type"]:
#             # Windows_Drivers_NXE_win_folder_prefix = y["folder_prefix"]
#             clone_repo(y["git"], None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12', y["type"])
#             # repo_name = y["type"]
#             # clear_git_win_driver_folder(y["type"])

#     # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle
#     path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_vmware//bundle"
#     vmware_distro1 = os.listdir(path)
#     print(vmware_distro1)
#     for x in vmware_distro1:
#         # if x.startswith("release_2"):
#         src_vmware_driver_path = path + "//" + x + "//signed"
#         # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle\async_80_bundle\signed
#         vmware_package_zip = os.listdir(src_vmware_driver_path)
#         print(vmware_package_zip)
#         # os.system('7z x C://Users//choutin//Downloads//' + NXE_OPT + ".zip" ' -y -oC://Users//choutin//Downloads//' + NXE_OPT)
#         cmd = '7z x ' + src_vmware_driver_path + vmware_package_zip + ' -y -o' + src_vmware_driver_path
#         print(cmd)
#         os.system(cmd)
#         # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle\async_80_bundle\signed
#         split_folder_name = x.split("_")
#         print(split_folder_name[1])
#         # target_words = ["vSphere", float(split_folder_name[1])/10]
#         # target_folder_name = "vSphere" + str(float(split_folder_name[1])/10)
#         # repository_path = current_path  + "//" + repo_name + "//" + target_folder_name
#         tmpstr = "" #str(vmware_package_zip).replace(".zip", "")
#         print(src_vmware_driver_path + tmpstr)
#         print(repository_path)
#         command = ["cp", src_vmware_driver_path + tmpstr + "//" + "*.*", repository_path]
#         exec_cmd(command)

def do_Windows_Drivers_NXE():
    print('do_Windows_Drivers_NXE do_Windows_Drivers_NXE')
    brcm_nxe_opt=get_yaml()
    repo_name = ''
    for y in brcm_nxe_opt:
        if "Windows_Drivers_NXE" in y["type"]:
            Windows_Drivers_NXE_win_folder_prefix = y["folder_prefix"]
            clone_repo(y["git"], None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12', y["type"])
            repo_name = y["type"]
            clear_git_win_driver_folder(y["type"])

    # path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_windows//bnxtnd//signed"
    path = "C://Users//choutin//Downloads//" + NXE_OPT + "//drivers_windows//bnxtnd//signed"
    win_distro1 = os.listdir(path)
    print(win_distro1)
    componentlistw=set()
    for x in win_distro1:
        if x.startswith("release_2"):
            src_win_driver_path = path + "//" + x
            target_win_driver_folder_name = x.replace('release_', 'win')
            repository_path = current_path  + "//" + repo_name + "//" + target_win_driver_folder_name
            print(src_win_driver_path)
            print(repository_path)
            
            print("bnxtnd."+target_win_driver_folder_name.replace('win', "w").replace('0', "k"))
            componentlistw.add("bnxtnd."+target_win_driver_folder_name.replace('win', "w").replace('0', "k"))
            print("component:")
            print(componentlistw)
            command = ["cp", src_win_driver_path + "//" + "*.*", repository_path]
            exec_cmd(command)

    # with open("C://Users//choutin//Documents//project//brcm_nxe_linux_driver//my_file_W.txt", "a") as file:
    #         # Write the new content to the file
    #         file.write(componentlistw)
    #         file.write("\n")
def do_Linux_Drivers_NX1():
    print('do_Linux_Drivers_NX1 do_Linux_Drivers_NX1')

def do_Linux_Drivers_NXE():
    brcm_nxe_opt=get_yaml()
    print('brcm_nxe_opt brcm_nxe_opt')
    print(brcm_nxe_opt)
    Linux_Drivers_NXE_linux_os = ['rhel', 'suse']
    for y in brcm_nxe_opt:

        print(y)
        print(y["type"])
        if "Linux_Drivers_NXE" in y["type"]:
            Linux_Drivers_NXE_linux_folder_prefix = y["folder_prefix"]
            clone_repo(y["git"], None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12', y["type"])
            clear_git_kmps_folder(y["type"])
            clear_git_libbnxtre_folder()
            for z in y:
                # print('zzzzz')
                print(z)
                print(y[z])
                # Linux_Drivers_NXE_linux_folder_prefix = y["folder_prefix"]
                # clone_repo(y["git"], None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12')
                # print(z["folder_prefix"])
                # if z["folder_prefix"] == 'rhel':
                #     repo_to_clone = z["git"]
                #     clone_repo(repo_to_clone, None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12')
                #     clear_git_kmps_folder()
                #     clear_git_libbnxtre_folder()

    # print(brcm_nxe_opt)
    # for y in brcm_nxe_opt:
    #     if "HPCD" in y:
    #         for z in brcm_nxe_opt[y]:
    #             print(z)
    #             print(z["folder_prefix"])
    #             if z["folder_prefix"] == 'rhel':
    #                 repo_to_clone = z["git"]
    #                 clone_repo(repo_to_clone, None, 'MaySPP2025_Gen10Gen11Gen12', 'NovSPP2025_Gen10Gen11Gen12')
    #                 clear_git_kmps_folder()
    #                 clear_git_libbnxtre_folder()


    # exit
    # linux_os = ['rhel', 'suse']
    for linux_type in Linux_Drivers_NXE_linux_folder_prefix:
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

                        dest_full_path = dest_libbnxtre_distro_path + "//" + lib_folder_name

                        if os.path.isdir(dest_full_path):
                            print('yesssss')
                        else:
                            print(dest_full_path)
                            print('noooooo')
                            command = ["mkdir", dest_full_path]
                            exec_cmd(command)

                            command = ["mkdir", dest_full_path + "//" + "x86_64"]
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
                    print("linux component:")
                    print("bnxt." + x.partition('.')[0])
                    componentlist.add("bnxt." + x.partition('.')[0])
                    with open("C://Users//choutin//Documents//project//brcm_nxe_linux_driver//my_file.txt", "a") as file:
                        # Write the new content to the file
                        file.write("bnxt." + x.partition('.')[0])
                        file.write("\n")
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

if __name__ == "__main__":
    threads = list()
    print("eeee")
    # exit
    # do_Windows_Drivers_NXE()
    # x = threading.Thread(target=do_Linux_Drivers_NXE)
    # logging.info("Main    : before running thread")
    # y = threading.Thread(target=do_Windows_Drivers_NXE)
    # z = threading.Thread(target=do_VMware_Drivers_NXE, args = str(NXE_OPT))
    z = threading.Thread(target=do_VMware_Drivers_NXE, args = (str(NXE_OPT), args.baseline_branch, args.new_branch))
    # args=("my_string",)).start()
    # threads.append(x)
    # threads.append(y)
    
    # x.start()
    # y.start()

    z.start()

# do_Linux_Drivers_NXE()
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