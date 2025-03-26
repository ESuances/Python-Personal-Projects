import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import re

pdf = FPDF(orientation="P", unit="mm", format="A4") # We create the PDF

filepaths = glob.glob("TxTFiles/*txt") # We get the files from the local filepath

for filepath in filepaths:
    # We get the file name first to get the title of the document
    file = filepath[9:] # We eliminate the TxTFiles\ from the string
    file_name = file.split(".") # We split the string to get rid of the .txt
    pdf.add_page() # We add the page where the info of the said animal will be displayed
    pdf.set_font(family="Times", size=24, style="B") # We set the title format
    pdf.cell(w=0, h=12, txt=file_name[0].capitalize(), ln=1) # We set the filename on the title as we set it before
    pdf.ln(15)
    with open(filepath, "r") as file_local:
        text = file_local.readlines() # We get the text from the .txt file
        cleaned_text = re.sub(r'\[\d+\]', '', text[0]) # So this is how we remove the [number] got it from deepseek.
    pdf.set_font(family="Times", size=12) # We set the font for the text
    pdf.multi_cell(w=0, h=8, txt=cleaned_text) # We add the text from the file to the PDF

pdf.output(f"GeneratedPDFs/animals.pdf") # We output the file with all the information.

# COMPLETED BY MYSELF :D