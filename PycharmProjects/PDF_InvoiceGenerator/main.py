# Automation program, just get the data and produce the data, no need for a GUI
# To make a program, you have to think about the input data and the output
import pandas as pd
import glob

filepaths = glob.glob("Invoices/*xlsx") # The * means getting all the type of files in this case .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # This is in particular from pandas to read Excel files.
    print(df)