
#Import OS, Pandas, PyPDF2 for library support
import os
import pandas as pd
import PyPDF2
import glob
#Folder address changes /// SSA TSA MPR
input_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
output_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Output'
excel_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\XL1'

for file in os.listdir(input_folder):
    if file.endswith('.pdf'):
        with open(os.path.join(input_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                with open(os.path.join(output_folder, os.path.splitext(file)[0] + '.csv'), 'w') as csv_file:
                    csv_file.write(text)
                    print("PDF to CSV Complete")


# Loop through all CSV files in the input folder
for filename in os.listdir(output_folder):
    if filename.endswith('.csv'):
        # Read CSV file using Pandas
        df = pd.read_csv(os.path.join(output_folder, filename))
        
        # Create an ExcelWriter object
        with pd.ExcelWriter(os.path.join(excel_folder, filename.replace('.csv', '.xlsx')), engine='openpyxl') as writer:
            # Write the DataFrame to an Excel file
            df.to_excel(writer, index=False)