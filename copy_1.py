import os
import shutil
from os import path

def copy_files_recursive(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                copy_files_recursive(item_path, dest_dir)
            else:
                file_extension = os.path.splitext(item)[1]
                extension_dir = os.path.join(dest_dir, file_extension[1:])  
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)
                shutil.copy2(item_path, extension_dir)
    except Exception as e:
        print(f"Error: {e}")

copy_files_recursive('test', 'dest_dir_path')
