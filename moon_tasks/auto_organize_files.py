
import os
import shutil


def organize_folder(folder):
    file_types = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Archives': ['.zip', '.rar']
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    # add message to data lineage log file
                    # logging solution here
                    print(f'Moved {filename} to {folder_name}')


# organize_folder('/path/to/Downloads')

if __name__ == '__main__':
    organize_folder('/path/to/Downloads')

