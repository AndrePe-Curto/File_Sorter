import os
import shutil
import sys

# Get the current working directory and list all files
path = os.getcwd()
files = os.listdir(path)

# Get the full path of the script file
script_path = os.path.abspath(sys.argv[0])

# Set to store unique file extensions
unique_extensions = set()

# Iterate through files to extract extensions
for file in files:
    extension = os.path.splitext(file)[1]
    extension = extension.replace('.', '')  # Remove the dot from the extension
    
    if extension:
        unique_extensions.add(extension)

# Convert set to a list of folder names
folder_names = list(unique_extensions)
print(folder_names)

# Create folders based on extensions and move files
for folder in folder_names:
    folder_path = os.path.join(path, folder + " Files")
    if not os.path.exists(folder_path):
        print(f"Creating directory: {folder_path}")
        os.makedirs(folder_path)
    else:
        print(folder + " Files already exists")

# Move files to respective folders based on extensions
for file in files:
    file_path = os.path.abspath(os.path.join(path, file))
    if file_path != script_path:  # Exclude the script file itself
        extension = os.path.splitext(file)[1].replace('.', '')
        if extension:
            src_path = os.path.join(path, file)
            dest_folder = os.path.join(path, extension + " Files")
            dest_path = os.path.join(dest_folder, file)
            if not os.path.exists(dest_path):
                print(f"Moving {file} to {dest_folder}")
                shutil.move(src_path, dest_path)

# Wait for user input before exiting
input("Press Enter to exit...")
