import os
import shutil

def sort_files_by_string(src_folder, dest_folder1, search_string1):
    # Check if the destination folder exists, create it if not
    if not os.path.exists(dest_folder1):
        os.makedirs(dest_folder1)
    
    # List all files in the source folder
    for filename in os.listdir(src_folder):
        # Create the full path of the file
        file_path = os.path.join(src_folder, filename)

        # Proceed only if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Check if the string is in the filename
            if search_string1 in filename:
                # Define the destination path
                dest_path = os.path.join(dest_folder1, filename)
                
                # Move the file to the destination folder
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename}")

# Example usage
src_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
dest_folder1 = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\TSA'
search_string1 = 'TSA'  # Replace this with the string you're searching for in filenames

sort_files_by_string(src_folder, dest_folder1, search_string1)




def sort_files_by_string(src_folder, dest_folder2, search_string1):
    # Check if the destination folder exists, create it if not
    if not os.path.exists(dest_folder2):
        os.makedirs(dest_folder2)
    
    # List all files in the source folder
    for filename in os.listdir(src_folder):
        # Create the full path of the file
        file_path = os.path.join(src_folder, filename)

        # Proceed only if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Check if the string is in the filename
            if search_string1 in filename:
                # Define the destination path
                dest_path = os.path.join(dest_folder2, filename)
                
                # Move the file to the destination folder
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename}")

# Example usage
src_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
dest_folder2 = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\SSA'
search_string2 = 'SSA'  # Replace this with the string you're searching for in filenames

sort_files_by_string(src_folder, dest_folder2, search_string2)


def sort_files_by_string(src_folder, dest_folder3, search_string1):
    # Check if the destination folder exists, create it if not
    if not os.path.exists(dest_folder3):
        os.makedirs(dest_folder3)
    
    # List all files in the source folder
    for filename in os.listdir(src_folder):
        # Create the full path of the file
        file_path = os.path.join(src_folder, filename)

        # Proceed only if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Check if the string is in the filename
            if search_string1 in filename:
                # Define the destination path
                dest_path = os.path.join(dest_folder3, filename)
                
                # Move the file to the destination folder
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename}")

# Example usage
src_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
dest_folder3 = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\SSA'
search_string3 = 'SSA'  # Replace this with the string you're searching for in filenames

sort_files_by_string(src_folder, dest_folder3, search_string3)