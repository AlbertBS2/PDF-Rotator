import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def rotate_pdf(pdf_file, deg):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    # Rotate each page in the PDF file
    for page in pdf_reader.pages:
        page.rotate(deg)
        pdf_writer.add_page(page)

    # Save the rotated PDF file to a BytesIO object
    output = BytesIO()
    pdf_writer.write(output)
    output.seek(0)

    st.write(f"{pdf_file.name}  has been rotated clockwise by {deg} degrees.")

    return output


def main():
    st.set_page_config(page_title='PDF Rotator', page_icon=':page_with_curl:')

    st.title('PDF Rotator', )
    st.write('This app rotates a PDF file.')

    deg = st.number_input('Rotation angle in degrees (clockwise)', value=90, min_value=-360, max_value=360, step=90)
    if deg == 0:
        st.warning('Please enter a non-zero rotation angle.')

    # Upload PDF file
    pdf_file = st.file_uploader('Upload your PDF file', type=['pdf'], accept_multiple_files=False)

    if st.button("Rotate PDF", ):
        with st.spinner('Rotating PDF...'):
            if pdf_file is not None:
                pdf_out = rotate_pdf(pdf_file, int(deg))

                # Download the rotated PDF file
                st.download_button(
                    label='Download Rotated PDF',
                    data=pdf_out,
                    file_name=f"{pdf_file.name.replace('.pdf', '_rotated.pdf')}",
                    mime='application/pdf'
                )
            else:
                st.error('Please upload a PDF file.')


if __name__ == '__main__':
    main()
