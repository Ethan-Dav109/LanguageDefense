#  **Defense Language File Converter** 
#
# **Code Explanation** 
#  
#  The Converter program is rather simple in what it does. First
#  it take in PDF files from the input folder, then converts them 
#  into CSV files, then outputs them into the Output folder. 
#  Finally the program then takes all the CSV files in the Output 
#  folder and convert them into the XL1 folder as XLSX files.
#
# **Needed Imports for functions and libraries**
import os
import pandas as pd
import PyPDF2
import glob
import csv
#
# **Folder Locations to be read from and written to**
input_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
output_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Output'
excel_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\XL1'
#
# **Meat of the program begins below**
#
#  The For loop opens the input folder
for file in os.listdir(input_folder):
#   If looks for files that ends in .pdf 
    if file.endswith('.pdf'):
#       The following With and For opens the PDF and saves the data
        with open(os.path.join(input_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
#  The second with takes the data and writes it into a CSV file,
#  it also output a message to notify of completion
                with open(os.path.join(output_folder, os.path.splitext(file)[0] + '.csv'), 'w') as csv_file:
                    csv_file.write(text)
                    print("PDF to CSV Complete")
#
#
#  The For loop opens the Output folder
for filename in os.listdir(output_folder):
#  This If statement looks for the CSV files in the Output folder
    if filename.endswith('.csv'):
#  This statement reads CSV file using Pandas
        df = pd.read_csv(os.path.join(output_folder, filename))
#  This statement creates an ExcelWriter object
        with pd.ExcelWriter(os.path.join(excel_folder, filename.replace('.csv', '.xlsx')), engine='openpyxl') as writer:
#  This statement writes the data to an Excel file
            df.to_excel(writer, index=False)
#
#  This For loop  searches for CSV files located in the output folder,
#  it will read the basename of the file and convert the name of
#  each file and replace the ending file identifier from .csv to .xlsx
for csv_file in glob.glob(os.path.join(output_folder, '*.csv')):
    csv_name = os.path.basename(csv_file)
    xlsx_name = csv_name.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(excel_folder, xlsx_name)
#  Pandas then reads the CSV files and saves the data and
#  stores the information. However a separator is needed due to pandas
#  reading the \A in the N\A as an actual line of code rather than
#  as text in the raw CSV file
    df = pd.read_csv(csv_file, sep = 'N\A')
# This statement writes the data to the XLSX file
    df.to_excel(xlsx_path, index=False)