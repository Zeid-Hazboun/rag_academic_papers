import PyPDF2
import mistune
import regex as re
from html import unescape
import sys
import os


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def clean_up_text(text):
    # Remove HTML entities
    text = unescape(text)
    # Remove <p> tags
    text = re.sub(r'<\/?p>', '', text)
    # Remove &quot;
    text = text.replace('&quot;', '"')
    # Remove any other HTML tags
    text = re.sub(r'<[^>]*>', '', text)
    # Remove any remaining special characters
    text = re.sub(r'&[^;]+;', '', text)
    return text

def convert_to_markdown(text):
    markdown = mistune.markdown(text)
    return markdown

def save_to_markdown(markdown_text, output_file):
    with open(output_file, 'w') as file:
        file.write(markdown_text)

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python3 pdf_to_markdown.py <pdf_file_path>")
    #     sys.exit(1)
    
    # #Taking pdf path from arguments
    # pdf_path = sys.argv[1]
    # markdown_output_path = "data/papers" + os.path.splitext(pdf_path)[0] + '.md'

    # text = extract_text_from_pdf(pdf_path)
    # cleaned_text = clean_up_text(text)
    # markdown = convert_to_markdown(cleaned_text)
    # save_to_markdown(markdown, markdown_output_path)


    if len(sys.argv) < 2:
        print("Usage: python3 pdf_to_markdown.py <folder_path>")
        sys.exit(1)

    # Taking folder path from arguments
    folder_path = sys.argv[1]

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            markdown_output_path = os.path.join("data/papers_md", os.path.splitext(filename)[0] + '.md')

            text = extract_text_from_pdf(pdf_path)
            cleaned_text = clean_up_text(text)
            markdown = convert_to_markdown(cleaned_text)
            save_to_markdown(markdown, markdown_output_path)