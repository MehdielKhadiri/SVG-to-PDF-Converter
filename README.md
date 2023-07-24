# SVG-to-PDF-Converter

This repository contains a Python script for converting SVG files to PDF and then merging them into a single PDF file. This can be useful when you have multiple SVG files that need to be combined into a single document.

## Setup and Requirements

The application requires the following software and libraries:

- Python 3.6 or later
- svglib
- reportlab
- PyPDF2

To install the necessary libraries, you can use pip:

```bash
pip install svglib reportlab PyPDF2
```

## Usage

After installing the dependencies, you can run the script by modifying the parameters in the main function at the bottom of the script. Here's an example of how to use the script:

```python
if __name__ == "__main__":
   # Replace these paths with the path to your SVG files and the desired output path for the merged PDF
   svg_directory = "path/to/svg/files" 
   output_pdf_path = "path/to/output.pdf"
   
   main(svg_directory, output_pdf_path)
```

Replace "path/to/svg/files" with the path to the directory containing your SVG files. Replace "path/to/output.pdf" with the desired output path for the merged PDF file.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
