'''This module provides functionality for backing up files older than 30 days'''
import os
import shutil
import time

def backup_old_files(src, dest):
    ''' This function backups files older than 30 days from src to dest '''
    current_time = time.time()
    for file in os.listdir(src):
        file_path = os.path.join(src, file)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > 30 * 86400:
                shutil.copy(file_path, dest)
                print(f"Backed up {file} to {dest}")
                os.remove(file_path)
                print(f"Deleted {file} from {src}")


file_src = "C:\\python\\"
file_dest = "C:\\temp\\"

backup_old_files(file_src, file_dest)