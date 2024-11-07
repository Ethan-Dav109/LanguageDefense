# LanguageDefense

# This folder and file is for the Literate Programming class of Fall 2024. The students involved are Ethan Davis, Cole Gernaat, and Ben Beaugrand.
# The specific problem in question is from the Defense Language Institute. They are asking for a program that will read the tables inside of PDF
# files that have been scrubbed clean of any pertinent data, and then will convert them into an XLSX file in order to be analyzed for the institute
# to learn from. Presently, the program utilizes Tabula, Pandas, and PyDF2. Tabula takes all of the data from the tables to output to a CSV, 
# after that Pandas converts the entire csv into a readable xlsx file. PyPDF2 creates a backup of all of the text instances in a .txt file
# and will be repurposed to instead just take the text from the relevant feedback information.