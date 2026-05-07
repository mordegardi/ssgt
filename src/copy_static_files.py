import os
import shutil


def copy_static(from_dir, to_dir):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    else:
        is_to_dir_empty = len(os.listdir(to_dir)) == 0

        if not is_to_dir_empty:
            shutil.rmtree(to_dir)
            os.mkdir(to_dir)

    recursive_copy(from_dir, to_dir)


def recursive_copy(from_dir, to_dir):
    dir_content = os.listdir(from_dir)

    if len(dir_content) == 0:
        return None

    for item in dir_content:
        new_file_from = os.path.join(from_dir, item)
        new_file_to = os.path.join(to_dir, item)

        if os.path.isfile(new_file_from):
            print(f"Copying: {new_file_from} to {new_file_to}...")
            shutil.copy(f"{new_file_from}", f"{new_file_to}")
        else:
            print(f"Creating a new dir: {new_file_from} to {new_file_to}...")
            os.mkdir(new_file_to)

            recursive_copy(new_file_from, new_file_to)
