
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



# For the CSV file located in the output folder, it will read the basename of the file and it will 
# convert the name of each fild and replace it to an xlsx.
for csv_file in glob.glob(os.path.join(output_folder, '*.csv')):
    csv_name = os.path.basename(csv_file)
    xlsx_name = csv_name.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(excel_folder, xlsx_name)

    # Pandas then reads the csv file with a separator on the data
    # and it stores that information. There is a separator due to 
    # the fact that pandas and dataframes reads \A as an actual
    # line of code in the raw CSV file.
    df = pd.read_csv(csv_file, sep = 'N\A')

    #The dataframe created then takes the CSV file and information
    #and it converts it to an excel file type and path.
    df.to_excel(xlsx_path, index=False)