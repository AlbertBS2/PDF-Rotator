# PDF Rotator

This project provides a script to rotate all pages in a PDF file. It can also be used as a web app.

## Requirements

- Python 3.x
- PyPDF2 library
- Streamlit (for usage as an app)

## Usage
To run it as a web app, navigate to the folder where you saved the file and run:
```bash
python streamlit app_rotate_pdf.py
```

To run is at a python script:

1. Place your PDF file in the specified input directory.

2. Update the dir_in and file_in variables in the script to match the input directory and PDF file name.

3. Specify the output directory by updating the dir_out variable.

4. Specify the degrees of rotation (clockwise) by updating the deg variable.

5. Run the script to generate the rotated PDF file.
