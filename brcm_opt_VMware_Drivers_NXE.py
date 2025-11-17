import os
from datetime import datetime
from util import exec_cmd, clone_repo, git_commit

current_path=os.getcwd()
tool_location = os.getcwd()

def clear_git_vmware_driver_folder(repo_name):
    current_path = os.getcwd()
    vmware_driver_folder = os.listdir(current_path)

    for x in vmware_driver_folder:
        if (x.startswith("vSphere") and os.path.isdir(current_path + "//" + x)):
            del_path = current_path + "//" + x
            command = ["rm", del_path + "//" + "*.zip"]
            exec_cmd(command)
            
def do_VMware_Drivers_NXE(drop_location, baseline_branch, new_branch):
    repo_name = "Broadcom-Optimized-VMware_Drivers_NXE"
    clone_repo("https://github.hpe.com/hpe/Broadcom-Optimized-VMware_Drivers_NXE.git", None, baseline_branch, new_branch, repo_name)
    clear_git_vmware_driver_folder(repo_name)

    # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle
    path = drop_location + "//drivers_vmware//bundle"
    vmware_distro1 = os.listdir(path)
    for x in vmware_distro1:
        src_vmware_driver_path = path + "//" + x + "//signed"
        # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle\async_80_bundle\signed
        vmware_package_zip = os.listdir(src_vmware_driver_path)
        print(vmware_package_zip)
        for package in vmware_package_zip:
            # if (len(vmware_package_zip) == 1):
            if "-package.zip" in package: # Broadcom-bnxt-Net-RoCE_233.0.256.0-1OEM.800.1.0.20613240_24674977-package.zip
                cmd = '7z x ' + src_vmware_driver_path + "//" + package + ' -y -o' + src_vmware_driver_path
                print(cmd)
                os.system(cmd)
 
                # C:\Users\choutin\Downloads\HPCD_v235.0.4.1\drivers_vmware\bundle\async_80_bundle\signed
                split_folder_name = x.split("_")
                target_folder_name = "vSphere" + str(float(split_folder_name[1])/10)

                repository_path = current_path  + "//" + repo_name + "//" + target_folder_name
                print("vmware repository_path")
                print(repository_path)
                
                if not os.path.isdir(repository_path):
                    print(f"The directory '{repository_path}' does not exist.")
                    # dest_kmp_path = repository_path + "//" + "kmps"
                    
                    command = ["mkdir", repository_path]
                    exec_cmd(command)             

                # vendor_src = src_vmware_driver_path + "//" + package.replace("-package", "")
                vendor_src = src_vmware_driver_path + "//" + package.replace("-package", "") 
                repo_dest = repository_path
                print(vendor_src)
                print(repo_dest)
                command = ["cp", vendor_src, repo_dest]
                exec_cmd(command)

    now = datetime.now()
    print("before do_VMware_Drivers_NXE git commit")
    print(now)
    git_commit(path, new_branch)