import tabula
import pandas as pd

# convert PDF into CSV
tabula.convert_into("2388Max.pdf", "2388Max.csv", output_format="csv", pages='all')

read_file = pd.read_csv('2388Max.csv')
read_file.to_excel('2388Max.xlsx', index=None, header=True)