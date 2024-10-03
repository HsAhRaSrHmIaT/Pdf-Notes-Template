from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv('topics.csv')

pdf.add_page()
pdf.set_font('Courier', 'B', 50)
pdf.set_text_color(28, 28, 28)
pdf.cell(w=0, h=250, txt='NOTES', align='C', ln=5)

for index, row in topics.iterrows():
    pdf.add_page()

    #set header
    pdf.set_font('Courier', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'])
    pdf.line(11, 21, 198, 21)
    pdf.line(11, 22, 198, 22)
    for y in range(30, 290, 10):
        pdf.line(15, y, 198, y)
        pdf.ln(5)
        # Add a bullet point
        pdf.set_font('Arial', '', 20)
        pdf.cell(10, y, txt=chr(149), ln=0)
    #set footer
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 10, txt=row['Topic'], align='R')
    pdf.set_y(-15)
    pdf.cell(pdf.w-25, 10, txt="Page No. %s" %(pdf.page_no()-1), align='C', ln=0)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        for y in range(30, 290, 10):
            pdf.line(15, y, 198, y)
            pdf.ln(5)
            # Add a bullet point
            pdf.set_font('Arial', '', 20)
            pdf.cell(10, y, txt=chr(149), ln=0)
        #set footer
        pdf.set_y(-15)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 10, txt=row['Topic'], align='R')
        pdf.set_y(-15)
        pdf.cell(pdf.w-25, 10, txt="Page No. %s" %(pdf.page_no()-1), align='C')

pdf.output('topics.pdf')