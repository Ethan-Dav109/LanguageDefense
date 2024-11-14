#import tabula
#import pandas as pd
import PyPDF2
#Use Tabula to convert the PDF into a CSV
#tabula.convert_into("MPRAria.pdf", "MPRAria.csv", output_format="csv", pages='all')


#Use Pandas as pd to then read the CSV made and convert to excel.
#read_file = pd.read_csv('MPRAria.csv')
#read_file.to_excel('MPRAria.xlsx', index=None, header=True)


# csv.reader
# csv.writer



#import PyPDF2
#def pdf_to_text(pdf_path, output_txt):
#    # Open the PDF file in read-binary mode
#    with open(pdf_path, 'rb') as pdf_file:
#        # Create a PdfReader object instead of PdfFileReader
#        pdf_reader = PyPDF2.PdfReader(pdf_file)
#
#        # Initialize an empty string to store the text
#        text = ''
#
#        for page_num in range(len(pdf_reader.pages)):
#            page = pdf_reader.pages[page_num]
#            text += page.extract_text()
#
#    # Write the extracted text to a text file
#    with open(output_txt, 'w', encoding='utf-8') as txt_file:
#        txt_file.write(text)
#
#if __name__ == "__main__":
#    pdf_path = 'MPRAria.pdf'
#
#    output_txt = 'MPRAria.txt'
#
#    pdf_to_text(pdf_path, output_txt)
#
#    print("PDF converted to text successfully!")


import os
import PyPDF2

input_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Input'
output_folder = r'C:\Users\twine\Documents\GitHub\LanguageDefense\Output'

for file in os.listdir(input_folder):
    if file.endswith('.pdf'):
        with open(os.path.join(input_folder, file), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                with open(os.path.join(output_folder, os.path.splitext(file)[0] + '.txt'), 'w') as txt_file:
                    txt_file.write(text)