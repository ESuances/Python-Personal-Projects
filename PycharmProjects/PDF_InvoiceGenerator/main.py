# Automation program, just get the data and produce the data, no need for a GUI
# To make a program, you have to think about the input data and the output
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*xlsx") # The * means getting all the type of files in this case .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # This is in particular from pandas to read Excel files.
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem[:5] # We get the name of the file by using this library.
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{filename}") # Title of the PDF
    pdf.output(f"GeneratedPDFs/{filename}.pdf") # Name of the PDF and where it would be outputed.