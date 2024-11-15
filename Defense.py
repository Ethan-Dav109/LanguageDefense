# ---------------------Import and Variable Name Area --------------------------------------- 
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



# ---------------------Below Is the Code and the File Sorter Area --------------------------------------- 


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







# ---------------------Converter Area --------------------------------------- 

#TSA
for file in os.listdir(tsa_folder):
    if file.endswith('.pdf'):
        with open(os.path.join(tsa_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                with open(os.path.join(tsa_folder, os.path.splitext(file)[0] + '.csv'), 'w') as csv_file:
                    csv_file.write(text)
                    print("PDF to CSV Complete")



# For the CSV file located in the output folder, it will read the basename of the file and it will 
# convert the name of each file and replace it to an xlsx.
for csv_file in glob.glob(os.path.join(tsa_folder, '*.csv')):
    csv_name = os.path.basename(csv_file)
    xlsx_name = csv_name.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(tsaxl_folder, xlsx_name)

    # Pandas then reads the csv file with a separator on the data
    # and it stores that information. There is a separator due to 
    # the fact that pandas and dataframes reads \A as an actual
    # line of code in the raw CSV file.
    df = pd.read_csv(csv_file, sep = 'N\A', engine = 'python')
    
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

                with open(os.path.join(ssa_folder, os.path.splitext(file)[0] + '.csv'), 'w') as csv_file:
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