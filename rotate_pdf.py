import PyPDF2

# Path to the PDF file to be rotated
dir_in = ""
file_in = ""
path_in = dir_in + file_in

# Path and name for the rotated PDF file
dir_out = ""
file_out = file_in.replace('.pdf', '_rotated.pdf')
path_out = dir_out + file_out

# Open the PDF file
pdf_in = open(path_in, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_in)
pdf_writer = PyPDF2.PdfWriter()

# Rotate each page in the PDF file
for page in pdf_reader.pages:
    page.rotate(-90)
    pdf_writer.add_page(page)

# Save the rotated PDF file
pdf_out = open(path_out, 'wb')
pdf_writer.write(pdf_out)

pdf_out.close()
pdf_in.close()