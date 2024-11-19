# # Defense.py - A DLIW and MSU Programming Project
#
# ## Introduction:
#
# MSU was approached with the problem of solving an issue within the DLIW;
# separating and finding useful data within progress reports. These reports are
# split up between three different format: TSA, SSA, and MPR. In each of these
# formats is a slew of information that could be analyzed and turned into useful
# changes to the program. The solution of this is to write a program that could
# take any number of these files, separate them out based on their category,
# convert them into a excel file, and then use that excel file's data and AI in
# order to create necessary graphs to analyze from.
#
# ## The Code:
#
# ### Imports:
#
# Below here is the code makes this possible in order to properly run the code,
# however, a few variable names and imports will have to be set. In order to get
# these imports, the command console will have to be used.
#
# pip install pandas
#
# pip install PyPDF2
#
# pip install glob
#
# are the main functions used in this program. Of course, down below, the folder
# will need to be changed to the address path that is on the local machine that
# contains all of these individual files.
#Import OS, Pandas, PyPDF2 for library support
import os
import pandas as pd
import PyPDF2
import glob

#Folder address changes /// SSA TSA MPR
input_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
tsa_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\TSA'
ssa_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\SSA'
mpr_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\MPR'
tsaxl_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\TSA\tsaxl'
ssaxl_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\SSA\ssaxl'
mprxl_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\MPR\mprxl'



# ### Sorting:
#
# The second step is to sort the files and to place them into their own
# respective folders. This was achieved by writing three identical loops that
# would check if a destination folder for a file existed, create it if it
# didn't, then it would check through every single file for a key phrase. If it
# found that key phrase, in this case TSA, SSA, or MPR, then it would move that
# file to the respective folder.

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

src_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
dest_folder3 = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input\MPR'
search_string3 = 'MPR'  # Replace this with the string you're searching for in filenames

sort_files_by_string(src_folder, dest_folder3, search_string3)

# ### Conversion: 
#
# The conversion will then scan through those folders and begin to convert them
# into a CSV, which will then convert to a XLSX file. This is done automatically
# and it is placed within a NEW folder that is present.  There is an error
# present in this that overwrites the file in the With open statement! If you
# break the with open out of the loop into its new With, it will theoretically
# work. **Please do this.**

#TSA
for file in os.listdir(tsa_folder):
    if file.endswith('.pdf'):
        with open(os.path.join(tsa_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                with open(os.path.join(tsa_folder, os.path.splitext(file)[0] + '.csv'), 'w', encoding = 'utf-8') as csv_file:
                    csv_file.write(text)
                    print("PDF to CSV Complete")

# For the CSV file located in the output folder, it will read the basename of
# the file and it will convert the name of each file and replace it to an xlsx.
for csv_file in glob.glob(os.path.join(tsa_folder, '*.csv')):
    csv_name = os.path.basename(csv_file)
    xlsx_name = csv_name.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(tsaxl_folder, xlsx_name)

    # Pandas then reads the csv file with a separator on the data and it stores
    # that information. There is a separator due to the fact that pandas and
    # dataframes reads \\A as an actual line of code in the raw CSV file.
    df = pd.read_csv(csv_file, sep = 'N\A', engine = 'python')
    #Inside of the DF, using PD, you can make it more pretty with a lot of testing
    #The dataframe created then takes the CSV file and information
    #and it converts it to an excel file type and path.
    df.to_excel(xlsx_path, index=False)
    print('TSA CSV to XLSX Complete')

#SSA
for file in os.listdir(ssa_folder):
    if file.endswith('.pdf'):
        with open(os.path.join(ssa_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                with open(os.path.join(ssa_folder, os.path.splitext(file)[0] + '.csv'), 'w', encoding = 'utf-8') as csv_file:
                    csv_file.write(text)
                    print("PDF to CSV Complete")

for csv_file in glob.glob(os.path.join(ssa_folder, '*.csv')):
    csv_name = os.path.basename(csv_file)
    xlsx_name = csv_name.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(ssaxl_folder, xlsx_name)
    df = pd.read_csv(csv_file, sep = 'N\A', engine = 'python')
    df.to_excel(xlsx_path, index=False)
    print('SSA CSV to XLSX Complete')

#MPR
for file in os.listdir(mpr_folder):
    if file.endswith('.pdf'):
        with open(os.path.join(mpr_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                with open(os.path.join(mpr_folder, os.path.splitext(file)[0] + '.csv'), 'w', encoding = 'utf-8') as csv_file:
                    csv_file.write(text)
                    print("PDF to CSV Complete")

for csv_file in glob.glob(os.path.join(mpr_folder, '*.csv')):
    csv_name = os.path.basename(csv_file)
    xlsx_name = csv_name.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(mprxl_folder, xlsx_name)

    df = pd.read_csv(csv_file, sep = 'N\A', engine = 'python')

    df.to_excel(xlsx_path, index=False)
    print('MPR CSV to XLSX Complete')