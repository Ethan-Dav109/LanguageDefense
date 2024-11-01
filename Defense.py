from tabula import convert_into
table_file = r"2388Max.pdf"
output_csv = r"2388max.csv"
df = convert_into(table_file, output_csv, output_format='csv', lattice=True, stream=False, pages="all")