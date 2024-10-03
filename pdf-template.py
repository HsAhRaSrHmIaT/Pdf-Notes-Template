from fpdf import FPDF
import pandas as pd
import streamlit as st


def process_file(file):
    topics = pd.read_csv(file)
    # Check if the column name is not 'Topic' and rename it to 'Topic'
    if topics.columns[0] != 'Topic' and len(topics.columns) > 1:
        topics.rename(columns={topics.columns[0]: 'Topic'}, inplace=True)
    if topics.columns[1] != 'Pages' and len(topics.columns) > 1:
        topics.rename(columns={topics.columns[1]: 'Pages'}, inplace=True)

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()
    pdf.set_font('Courier', 'B', 50)
    pdf.set_text_color(28, 28, 28)
    pdf.cell(w=0, h=250, txt='NOTES', align='C', ln=5)

    for index, row in topics.iterrows():
        pdf.add_page()

        # set header
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
        # set footer
        pdf.set_y(-15)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 10, txt=row['Topic'], align='R')
        pdf.set_y(-15)
        pdf.cell(pdf.w - 25, 10, txt="Page No. %s" % (pdf.page_no() - 1), align='C', ln=0)

        for i in range(row['Pages'] - 1):
            pdf.add_page()

            for y in range(30, 290, 10):
                pdf.line(15, y, 198, y)
                pdf.ln(5)
                # Add a bullet point
                pdf.set_font('Arial', '', 20)
                pdf.cell(10, y, txt=chr(149), ln=0)
            # set footer
            pdf.set_y(-15)
            pdf.set_font('Arial', 'I', 8)
            pdf.cell(0, 10, txt=row['Topic'], align='R')
            pdf.set_y(-15)
            pdf.cell(pdf.w - 25, 10, txt="Page No. %s" % (pdf.page_no() - 1), align='C')

    pdf.output('topics.pdf')

    pdf = FPDF(orientation='P', unit='mm', format='A4')
st.header("Writing Notes Template Generator")
# Create a file uploader
file = st.file_uploader("Upload a CSV File", type=['csv'])
st.markdown("(Please upload a CSV file with the following columns: 'Topic' and 'Pages')")
st.write("For example: ")
df = pd.DataFrame({'Topic': ['Math', 'Science'], 'Pages': [5, 10]})
st.markdown(df.to_html(index=False), unsafe_allow_html=True)

if file is not None:
    process_file(file)
    st.write("PDF file created successfully!")
    # Create a download button for the PDF file
    with open('topics.pdf', 'rb') as f:
        pdf_file = f.read()
    st.download_button(
        label="Download PDF file",
        data=pdf_file,
        file_name='Template.pdf',
        mime='application/pdf'
    )
