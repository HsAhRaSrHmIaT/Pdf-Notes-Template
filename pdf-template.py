from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

topics = pd.read_csv('topics.csv')

for index, row in topics.iterrows():
    pdf.add_page()
    pdf.set_font('Courier', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'])
    pdf.line(11, 22, 198, 22)


pdf.output('topics.pdf')