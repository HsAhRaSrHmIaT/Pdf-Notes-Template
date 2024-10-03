from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv('topics.csv')

for index, row in topics.iterrows():
    pdf.add_page()

    #set header
    pdf.set_font('Courier', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'])
    pdf.line(11, 22, 198, 22)

    #set footer
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 10, txt=row['Topic'], align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        #set footer
        pdf.set_y(-15)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 10, txt=row['Topic'], align='R')

pdf.output('topics.pdf')