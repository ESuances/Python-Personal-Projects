# Automation program, just get the data and produce the data, no need for a GUI
# To make a program, you have to think about the input data and the output
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*xlsx") # The * means getting all the type of files in this case .xlsx

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem # We get the filename from that library
    invoice_num, date = filename.split('-')
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_num}", ln=1) # Title of the PDF
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)  # Get the date from the same name but after the split.
    df = pd.read_excel(filepath, sheet_name="Sheet 1")  # This is in particular from pandas to read Excel files.
    pdf.ln()

    # We create the header of all the columns this way
    columns = list(df.columns)
    pdf.set_font(family="Times", size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0].replace('_', ' ').title(), border=1, align='C')
    pdf.cell(w=65, h=8, txt=columns[1].replace('_', ' ').title(), border=1, align='C') # I don't do a for loop because of the w size on this one
    pdf.cell(w=32, h=8, txt=columns[2].replace('_', ' ').title(), border=1, align='C') # And this one
    pdf.cell(w=30, h=8, txt=columns[3].replace('_', ' ').title(), border=1, align='C')
    pdf.cell(w=30, h=8, txt=columns[4].replace('_', ' ').title(), border=1, align='C')
    pdf.ln()

    total_sum = 0

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1, align='C')
        pdf.cell(w=65, h=8, txt=str(row["product_name"]), border=1, align='C')
        pdf.cell(w=32, h=8, txt=str(row["amount_purchased"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, align='C')
        total_sum = row["total_price"] + total_sum # We get the value of all the added prices
        pdf.ln()

    pdf.cell(w=157, h=8)
    pdf.cell(w=30, h=8, txt=str(total_sum), border = 1, align = 'C')


    pdf.output(f"GeneratedPDFs/{invoice_num}.pdf") # Name of the PDF and where it would be outputed.