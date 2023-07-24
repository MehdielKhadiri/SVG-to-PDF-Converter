import os
import glob
import time
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfMerger

def svg_to_pdf(svg_path, pdf_path):
    # Convert a single SVG file to PDF
    try:
        drawing = svg2rlg(svg_path)
        renderPDF.drawToFile(drawing, pdf_path)
        print(f'Successfully converted {svg_path} to {pdf_path}.')
        time.sleep(1)  # Wait a bit for the file to write to disk
    except Exception as e:
        print(f'Failed to convert {svg_path} to {pdf_path}. Error: {e}')

def merge_pdfs(pdf_files, output_path):
    # Merge multiple PDF files into one
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

def main(svg_dir, output_pdf):
    # Convert SVGs to PDFs
    svg_files = sorted(glob.glob(os.path.join(svg_dir, '*.svg')), key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    pdf_files = []

    for svg_file in svg_files:
        pdf_file = svg_file.replace('.svg', '.pdf').replace('\\', '/')
        pdf_files.append(pdf_file)
        svg_to_pdf(svg_file, pdf_file)

    # Merge PDFs
    merge_pdfs(pdf_files, output_pdf)

    # Delete individual PDFs
    for pdf_file in pdf_files:
        os.remove(pdf_file)

if __name__ == "__main__":
    # Replace these paths with the path to your SVG files and the desired output path for the merged PDF
    svg_directory = "C:/Users/banjo/Downloads/En-tête(2)" 
    output_pdf_path = "C:/Users/banjo/OneDrive/Bureau/output1.pdf"
    
    main(svg_directory, output_pdf_path)


