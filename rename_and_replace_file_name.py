import os

def rename_and_replace(path, old_substring, new_substring):
    for root, dirs, files in os.walk(path):
        for file in files:
            if old_substring in file:
                new_file = file.replace(old_substring, new_substring)
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")

        for dir in dirs:
            if old_substring in dir:
                new_dir = dir.replace(old_substring, new_substring)
                old_path = os.path.join(root, dir)
                new_path = os.path.join(root, new_dir)
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")

# Example usage
path = "C:\\Users\\U3F\\Desktop\\polices\\stream"
old_substring = "pjugg"
new_substring = "dtpjugg"
rename_and_replace(path, old_substring, new_substring)
