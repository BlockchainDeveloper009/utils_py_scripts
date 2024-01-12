import os

def compare_directories(dir1, dir2):
    # Get the list of filenames in each directory
    files_dir1 = set(os.listdir(dir1))
    files_dir2 = set(os.listdir(dir2))

    # Find common and unique files
    common_files = files_dir1.intersection(files_dir2)
    unique_files_dir1 = files_dir1 - files_dir2
    unique_files_dir2 = files_dir2 - files_dir1

    # Display the results
    print(f"Common files: {common_files}")
    print(f"Files unique to {dir1}: {unique_files_dir1}")
    print(f"Files unique to {dir2}: {unique_files_dir2}")

# Replace 'path/to/dir1' and 'path/to/dir2' with the actual directory paths
directory1 = 'path/to/dir1'
directory2 = 'path/to/dir2'

compare_directories(directory1, directory2)
