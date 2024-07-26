import requests
import camelot
import pandas as pd
import tempfile
import re
from pathlib import Path


def get_data():
    # URL of the PDF file
    pdf_url = 'https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap04.pdf'

    # Download the PDF file
    response = requests.get(pdf_url)
    response.raise_for_status()  # Check if the request was successful

    # Save the PDF content to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf_file:
        temp_pdf_file.write(response.content)
        temp_pdf_path = temp_pdf_file.name

    # Extract tables from the specific page using Camelot
    # Adjust page numbers according to zero-based indexing (e.g., page 16 corresponds to page number 15)
    tables = camelot.read_pdf(temp_pdf_path, pages='16', flavor='stream')

    # Function to sanitize sheet names
    def sanitize_sheet_name(name):
        # Remove illegal characters and trim to 31 characters
        sanitized_name = re.sub(r'[\/:*?\[\]]', '', name)[:31]
        if sanitized_name == '':
            sanitized_name = 'Sheet1'  # Default name if sanitized name is empty
        return sanitized_name

    # Save each table to a separate sheet in an Excel file
    excel_path = 'tables_page_16.xlsx'
    with pd.ExcelWriter(excel_path, engine='openpyxl') as excel_writer:
        for i, table in enumerate(tables):
            df = table.df
            # Create a sanitized sheet name for each table
            sheet_name = sanitize_sheet_name(f'Table_{i + 1}')
            # Write DataFrame to a sheet in the Excel file
            df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

    print(f"Tables from page 16 have been processed and saved to {excel_path}.")
