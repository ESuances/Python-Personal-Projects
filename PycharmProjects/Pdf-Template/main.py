from fpdf import FPDF
import pandas as pd

# Rest day, will delete tomorrow

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B",size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10,21,200,21)
    for x in range(0, 270, 10):
        pdf.line(10, x + 21, 200, x + 21)

    # Set footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for x in range(row["Pages"] - 1):
        pdf.add_page()
        # Set footer
        for i in range(0, 270, 10):
            pdf.line(10, i + 21, 200, i + 21)
        pdf.ln(270)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")