import yaml
import subprocess
import os

# from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow
# from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication


# class MultipleInputDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Multiple Input Dialog")
#         self.setup_ui()
#         self.results = {} # Dictionary to store input values

#     def setup_ui(self):
#         main_layout = QVBoxLayout()

#         # Input 1: QLineEdit for text
#         name_layout = QHBoxLayout()
#         name_label = QLabel("Name:")
#         self.name_input = QLineEdit()
#         name_layout.addWidget(name_label)
#         name_layout.addWidget(self.name_input)
#         main_layout.addLayout(name_layout)

#         # Input 2: QLineEdit for age (with validator for integers)
#         age_layout = QHBoxLayout()
#         age_label = QLabel("Age:")
#         self.age_input = QLineEdit()
#         # Optional: Add a QIntValidator for integer input
#         # from PyQt5.QtGui import QIntValidator
#         # self.age_input.setValidator(QIntValidator(0, 150, self))
#         age_layout.addWidget(age_label)
#         age_layout.addWidget(self.age_input)
#         main_layout.addLayout(age_layout)

#         # Buttons (OK/Cancel)
#         button_layout = QHBoxLayout()
#         ok_button = QPushButton("OK")
#         cancel_button = QPushButton("Cancel")
#         button_layout.addStretch(1) # Pushes buttons to the right
#         button_layout.addWidget(ok_button)
#         button_layout.addWidget(cancel_button)
#         main_layout.addLayout(button_layout)

#         self.setLayout(main_layout)

#         # Connect signals to slots
#         ok_button.clicked.connect(self.accept)
#         cancel_button.clicked.connect(self.reject)

#     def accept(self):
#         self.results['name'] = self.name_input.text()
#         self.results['age'] = self.age_input.text() # Convert to int if needed
#         super().accept()

# if __name__ == '__main__':
#     app = QApplication([])
#     dialog = MultipleInputDialog()
#     if dialog.exec_() == QDialog.Accepted:
#         print("Inputs received:", dialog.results)
#     else:
#         print("Dialog cancelled.")
#     # app.exec_()
#     app.quit()

# def get_multiple_inputs_pyqt():
#     app = QApplication([])
    
#     name, ok1 = QInputDialog.getText(None, "Input", "Enter your name:")
#     age, ok2 = QInputDialog.getInt(None, "Input", "Enter your age:")
#     language, ok3 = QInputDialog.getItem(None, "Input", "Select a language:", ["Python", "Java", "C++"], 0, False)

#     if ok1 and ok2 and ok3:
#         print(f"Name: {name}, Age: {age}, Language: {language}")
#     else:
#         print("Input cancelled or incomplete.")

#     app.quit()

# # Call the function
# get_multiple_inputs_pyqt()

# import tkinter as tk
# from tkinter import simpledialog

# # Create a Tkinter window
# window = tk.Tk()
# # Hide the main window, as we only need the dialog
# window.withdraw() 

# # Create an input dialog and get user input
# user_input = simpledialog.askstring("Input Dialog", "Enter your name:")
# user_input2 = simpledialog.askstring("Input Dialog", "Enter your name2:")

# # Check if the user entered anything (or clicked Cancel)
# if user_input and user_input2 is not None:
#     print(f"Hello, {user_input}!")
# else:
#     print("No input provided.")

# Run the Tkinter event loop (optional, as withdraw() means no visible window)
# window.mainloop() 



current_path = os.getcwd()

brcm_nxe_opt = ""
repository_path = current_path + "//" + "Linux_Drivers_NXE"
# "C://Users//choutin//Documents//Linux_Drivers_NXE"
# os.system('7z x C://Users//choutin//Downloads//HPCD_v235.0.1.1.zip -y -oC://Users//choutin//Downloads//HPCD_v235.0.1.1')

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

    # try:
    #     subprocess.run(command, check=True, capture_output=True, text=True)
    #     print(f"Repository '{repo_url}' cloned successfully.")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error cloning repository: {e}")
    #     print(f"Stderr: {e.stderr}")
    # except FileNotFoundError:
    #     print("Error: 'git' command not found. Ensure Git is installed and in your PATH.")
    
    repository_path = current_path + "//Linux_Drivers_NXE"
    # "C://Users//choutin//Documents//Linux_Drivers_NXE"
    os.chdir(repository_path)
    # command1 = ["ls"] 

    # try:
    #     print(command1)
    #     subprocess.run(command1, check=True, capture_output=True, text=True)
    #     # print(f"11 Repository '{repo_url}' cloned successfully.")
    # except subprocess.CalledProcessError as e:
    #     print(f"11 Error cloning repository: {e}")
    #     print(f"11 Stderr: {e.stderr}")
    # except FileNotFoundError:
    #     print("11 Error: 'git' command not found. Ensure Git is installed and in your PATH.")     

    command = ["git", "switch", src_branch]
    # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
    exec_cmd(command)

    command = ["git", "checkout", "--orphan", target_branch]
    exec_cmd(command)
    # try:
    #     subprocess.run(command, check=True, capture_output=True, text=True)
    #     print(f"Repository '{repo_url}' cloned successfully.")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error cloning repository: {e}")
    #     print(f"Stderr: {e.stderr}")
    # except FileNotFoundError:
    #     print("Error: FileNotFoundError") 
        # print("Error: 'git' command not found. Ensure Git is installed and in your PATH.") 

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

            # try:
            #     subprocess.run(command, check=True, capture_output=True, text=True)
            #     print(f"clear_git_folder Repository '{git_f}' cloned successfully.")
            # except subprocess.CalledProcessError as e:
            #     print(f"clear_git_folder Error cloning repository: {e}")
            #     print(f"clear_git_folder Stderr: {e.stderr}")
            # except FileNotFoundError:
            #     print("clear_git_folder Error: 'git' command not found. Ensure Git is installed and in your PATH.")

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

                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"clear_git_libbnxtre_folder Repository '{git_f}' cloned successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"clear_git_libbnxtre_folder Error cloning repository: {e}")
                    #     print(f"clear_git_libbnxtre_folder Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("clear_git_libbnxtre_folder Error: 'git' command not found. Ensure Git is installed and in your PATH.")

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
    # try:
    #     subprocess.run(command, check=True, capture_output=True, text=True)
    #     print(f"Repository '{repo_url}' cloned successfully.")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error cloning repository: {e}")
    #     print(f"Stderr: {e.stderr}")
    # except FileNotFoundError:
    #     print("Error: 'git' command not found. Ensure Git is installed and in your PATH.")
    
    repository_path = current_path + "//Linux_Drivers_NXE"
    # "C://Users//choutin//Documents//Linux_Drivers_NXE"
    os.chdir(repository_path)
    command1 = ["ls"] 
    # "cd C:\\Users\\choutin\\Documents\\Linux_Drivers_NXE", 
    # subprocess.run(command, check=True, capture_output=True, text=True)
    # command = ["git", "switch", src_branch]

    # try:
    #     print(command1)
    #     subprocess.run(command1, check=True, capture_output=True, text=True)
    #     # print(f"11 Repository '{repo_url}' cloned successfully.")
    # except subprocess.CalledProcessError as e:
    #     print(f"11 Error cloning repository: {e}")
    #     print(f"11 Stderr: {e.stderr}")
    # except FileNotFoundError:
    #     print("11 Error: 'git' command not found. Ensure Git is installed and in your PATH.")   
 

    command = ["git", "switch", src_branch]
    # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
    exec_cmd(command)
    # try:
    #     subprocess.run(command, check=True, capture_output=True, text=True)
    #     print(f"Repository '{repo_url}' cloned successfully.")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error cloning repository: {e}")
    #     print(f"Stderr: {e.stderr}")
    # except FileNotFoundError:
    #     print("Error: FileNotFoundError") 

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
                # clear_git_kmps_folder()
                clear_git_libbnxtre_folder()



linux_os = ['rhel', 'suse']
for linux_type in linux_os:
    rhel_arr1 = os.listdir('C://Users//choutin//Downloads//HPCD_v235.0.1.1//drivers_linux//bnxt_rocelib//rpm' + "//"  + linux_type)
    print(rhel_arr1)
    for x in rhel_arr1:
        path = "C://Users//choutin//Downloads//HPCD_v235.0.1.1//drivers_linux//bnxt_rocelib//rpm" + "//" + linux_type + "//" + x
        linux_distro1 = os.listdir(path)
        # print('===------')
        for y in linux_distro1:
            # print(linux_distro1)
            substrings_to_avoid = ["debug", "devel", "src"]
            if (y.startswith("libbnxt_re-") and all(sub not in y for sub in substrings_to_avoid)):
                print('===------')
                print(y)
                directory_path = repository_path + "//" + "libbnxtre" + "//" + x.partition('.')[0]
                print(directory_path)
                if os.path.isdir(directory_path):
                    print(f"suse The directory '{directory_path}' exists.")
                    rhel_path = repository_path + "//" + "libbnxtre"
                    path2 = rhel_path + "//" + x.partition('.')[0]
                    lib_folder_name = ''
                    if linux_type == 'rhel':
                        lib_folder_name = x.replace('.', 'u')
                    elif linux_type == 'suse':
                        lib_folder_name = x.replace('.', 'sp')

                    
                    path3 = path2 + "//" + lib_folder_name

                    if os.path.isdir(path3):
                        print('yesssss')
                    else:
                        print(path3)
                        print('noooooo')
                        command = ["mkdir", path3]
                        exec_cmd(command)
                        # try:
                        #     subprocess.run(command, check=True, capture_output=True, text=True)
                        #     print(f"suse mkdir file successfully.")
                        # except subprocess.CalledProcessError as e:
                        #     print(f"suse mkdir Error cloning repository: {e}")
                        #     print(f"suse mkdir Stderr: {e.stderr}")
                        # except FileNotFoundError:
                        #     print("suse mkdir Error: FileNotFoundError") 

                        command = ["mkdir", path3 + "//" + "x86_64"]
                        exec_cmd(command)
                        # try:
                        #     subprocess.run(command, check=True, capture_output=True, text=True)
                        #     print(f"suse mkdir file successfully.")
                        # except subprocess.CalledProcessError as e:
                        #     print(f"suse mkdir Error cloning repository: {e}")
                        #     print(f"suse mkdir Stderr: {e.stderr}")
                        # except FileNotFoundError:
                        #     print("suse mkdir Error: FileNotFoundError") 


                    # del_path = directory_path + "//" + "x86_64"
                    # print(del_path)
                    # os.chdir(del_path)
                    # command = ["rm", "*.rpm"]
                    # # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"del file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"del Error cloning repository: {e}")
                    #     print(f"del Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("del Error: FileNotFoundError") 
                else:
                    print(f"suse The directory '{directory_path}' does not exist.")
                    rhel_path = repository_path + "//" + "libbnxtre"
                    # rhel_path = repository_path + "//" + "libbn.xtre" + "//" + x.partition('.')[0]
                    
                    # print(rhel_path) 

                    os.chdir(rhel_path)
                    
                    command = ["mkdir", x.partition('.')[0]]
                    exec_cmd(command)
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"suse mkdir file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"suse mkdir Error cloning repository: {e}")
                    #     print(f"suse mkdir Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("suse mkdir Error: FileNotFoundError") 
                    path2 = rhel_path + "//" + x.partition('.')[0]
                    os.chdir(path2)
                    # lib_folder_name = x.replace('.', 'u')
                    if linux_type == 'rhel':
                        lib_folder_name = x.replace('.', 'u')
                    elif linux_type == 'suse':
                        lib_folder_name = x.replace('.', 'sp')
                    command = ["mkdir", lib_folder_name]
                    exec_cmd(command)
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"susemkdir file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"susemkdir Error cloning repository: {e}")
                    #     print(f"susemkdir Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("susemkdir Error: FileNotFoundError") 
                    
                    path3 = path2 + "//" + lib_folder_name
                    os.chdir(path3)
                    command = ["mkdir", "x86_64"]
                    exec_cmd(command)
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"susemkdir file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"susemkdir Error cloning repository: {e}")
                    #     print(f"susemkdir Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("susemkdir Error: FileNotFoundError") 
                # src_path_to_target =  
                print("xxxxxxxxxx")
                target_path = path3 + "//" + "x86_64"
                print(target_path)
                src_path = path + "//" + y
                print(src_path)


                print("cp 451")
                command = ["cp", src_path, target_path]
                exec_cmd(command)
                # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
                # try:
                #     subprocess.run(command, check=True, capture_output=True, text=True)
                #     print(f"copy file successfully.")
                # except subprocess.CalledProcessError as e:
                #     print(f"Error cloning repository: {e}")
                #     print(f"Stderr: {e.stderr}")
                # except FileNotFoundError:
                #     print("Error: FileNotFoundError") 


exit

linux_os = ['rhel', 'suse']
for linux_type in linux_os:
    rhel_arr1 = os.listdir('C://Users//choutin//Downloads//HPCD_v235.0.1.1//drivers_linux//bundle//kmp//' + linux_type)
    print(rhel_arr1)
    for x in rhel_arr1:
        path = "C://Users//choutin//Downloads//HPCD_v235.0.1.1//drivers_linux//bundle//kmp//" + linux_type + "//" + x
        linux_distro1 = os.listdir(path)
        print('------')
        print(linux_distro1)
        print('------')
        for y in linux_distro1:
            # path = "C://Users//choutin//Downloads//HPCD_v235.0.1.1//drivers_linux//bundle//kmp//rhel" + "//" + x + "//" + y
            # print(y)
            if (linux_type == 'rhel' and y.startswith("kmod-bnxt_en") and "debuginfo" not in y) or (linux_type == 'suse' and y.startswith("bnxt_en-kmp-default") and "debuginfo" not in y):
                print(y)
                # copy_to_git_folder(y) "C://Users//choutin//Documents//Linux_Drivers_NXE"
                
                directory_path = repository_path + "//" + "kmps" + "//" + x.partition('.')[0]
                if os.path.isdir(directory_path):
                    print(f"dell The directory '{directory_path}' exists.")
                    # del_path = directory_path + "//" + "x86_64"
                    # print(del_path)
                    # os.chdir(del_path)
                    # command = ["rm", "*.rpm"]
                    # # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"del file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"del Error cloning repository: {e}")
                    #     print(f"del Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("del Error: FileNotFoundError") 
                else:
                    print(f"The directory '{directory_path}' does not exist.")
                    rhel_path = repository_path + "//" + "kmps"
                    os.chdir(rhel_path)
                    
                    command = ["mkdir", x.partition('.')[0]]
                    exec_cmd(command)
                    # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"mkdir file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"mkdir Error cloning repository: {e}")
                    #     print(f"mkdir Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("mkdir Error: FileNotFoundError") 
                    
                    os.chdir(directory_path)
                    command = ["mkdir", "x86_64"]
                    exec_cmd(command)
                    # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
                    # try:
                    #     subprocess.run(command, check=True, capture_output=True, text=True)
                    #     print(f"mkdir file successfully.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"mkdir Error cloning repository: {e}")
                    #     print(f"mkdir Stderr: {e.stderr}")
                    # except FileNotFoundError:
                    #     print("mkdir Error: FileNotFoundError") 
                
                target_path = repository_path + "//" + "kmps" + "//" + x.partition('.')[0] + "//" + "x86_64"
                print(target_path)
                src_path = path + "//" + y
                print(src_path)


                print("cp 536")
                command = ["cp", src_path, target_path]
                exec_cmd(command)
                # command = ["cd C://Users//choutin//Documents//Linux_Drivers_NXE", "git", "checkout --orphan", target_branch]
                # try:
                #     subprocess.run(command, check=True, capture_output=True, text=True)
                #     print(f"copy file successfully.")
                # except subprocess.CalledProcessError as e:
                #     print(f"Error cloning repository: {e}")
                #     print(f"Stderr: {e.stderr}")
                # except FileNotFoundError:
                #     print("Error: FileNotFoundError") 


        # files = os.listdir(path)
        # if files.startwith("kmod-bnxt_en"):
        #     print(files)
    # print(linux_distro1)
    # print("\n")
    # brcm_nxe_opt.get('clusters').get('test').get('tag_cl')
    # key = find_key_by_value(brcm_nxe_opt, "rhel")
    # brcm_nxe_opt=get_yaml()
    # print(brcm_nxe_opt)
    # for y in brcm_nxe_opt:
    #     if "HPCD" in y:
    #         # print(brcm_nxe_opt[y])
    #         # print(y)
    #         for z in brcm_nxe_opt[y]:
    #             # print(z)
    #             print(z["folder_prefix"])
    #         #     # print(y[folder_prefix])
    #             print("\n")


target_path = repository_path
print(target_path)
# print(os.chdir(target_path))
os.chdir(target_path)
print(current_path + "//" + "git_change.txt")
command = ["git", "status", ">>", target_path + "//" + "git_change.txt"]
exec_cmd(command)

import os

def delete_rpm_files(folder_path):
    """
    刪除指定資料夾及其所有子資料夾中的 .rpm 檔案

    :param folder_path: 要處理的根資料夾路徑
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.rpm'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

# 使用範例
# delete_rpm_files("/path/to/your/folder")