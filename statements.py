import re
import os
from PyPDF2 import PdfReader

def tidy_text(block):
    """
    Cleans up a list of text lines by removing unwanted substrings.
    """
    #print(block)
    cleaned_block = []
    block[5] = block[5].rstrip('.')
    for line in block:
        # Remove ',Description' and '.Type' etc exactly as written
        line = line.replace('.Description', '')
        line = line.replace('.Type', '')
        line = line.replace('.Money Out (£)', '')
        line = line.replace('.Balance (£)', '')
        line = line.replace('blank.', '0.00')
        line = line.replace('blank', '0.00')
        cleaned_block.append(line.strip())
    return cleaned_block


def list_pdf_files(folder_path):
    """
    Lists all PDF files in the given folder.
    """
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    return pdf_files


def extract_lines_with_dates_and_context(pdf_path, context_lines=5):
    """
    Opens a text-based PDF and returns all lines containing a date
    in the format '02 Apr 24' plus the following 'context_lines' lines.
    """
    date_pattern = re.compile(r"\b\d{2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}\b")
    matching_blocks = []

    reader = PdfReader(pdf_path)

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text:
            continue

        lines = text.splitlines()
        for i, line in enumerate(lines):
            if date_pattern.search(line):
                # Capture the line and up to 5 lines after it
                block = lines[i:i + context_lines + 1]
                block = tidy_text(block)
                print('"' + block[0] + '","' + block[1] + '","' + block[3] + '","' + block[4] + '","' + block[5] + '"')
                #print(block)
                matching_blocks.append({
                    "lines": block
                })

    return block


if __name__ == '__main__':
    folder_path = "/mnt/c/temp/"
    pdf_files = list_pdf_files(folder_path)
    for file in pdf_files:
        fullPath = folder_path + file
        # print(fullPath)
        matches = extract_lines_with_dates_and_context(fullPath)

    #pdf_path = "/mnt/c/temp/Statement_2024_7.pdf"
    #matches = extract_lines_with_dates_and_context(pdf_path)
    #print(matches)

