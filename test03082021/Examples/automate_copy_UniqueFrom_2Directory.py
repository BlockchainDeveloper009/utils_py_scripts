import os
import shutil

def compare_and_copy_unique_files(dir1, dir2, destination_dir):
    # Get the list of filenames in each directory
    files_dir1 = set(os.listdir(dir1))
    files_dir2 = set(os.listdir(dir2))

    # Find unique files in each directory
    unique_files_dir1 = files_dir1 - files_dir2
    unique_files_dir2 = files_dir2 - files_dir1

    # Copy unique files to the destination directory
    for filename in unique_files_dir1:
        source_path = os.path.join(dir1, filename)
        destination_path = os.path.join(destination_dir, filename)
        shutil.copy2(source_path, destination_path)
        print(f"Copied {filename} from {dir1} to {destination_dir}")

    for filename in unique_files_dir2:
        source_path = os.path.join(dir2, filename)
        destination_path = os.path.join(destination_dir, filename)
        shutil.copy2(source_path, destination_path)
        print(f"Copied {filename} from {dir2} to {destination_dir}")

# Replace 'path/to/dir1', 'path/to/dir2', and 'path/to/destination' with the actual directory paths
directory1 = 'path/to/dir1'
directory2 = 'path/to/dir2'
destination_directory = 'path/to/destination'

compare_and_copy_unique_files(directory1, directory2, destination_directory)
