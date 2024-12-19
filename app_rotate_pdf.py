import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

####################################################################### FUNCTIONS #######################################################################

def rotate_pdf(pdf_file, deg, range_pages=None):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    # Rotate pages in the PDF file
    i=1
    for page in pdf_reader.pages:
        if range_pages is None:
            page.rotate(deg)
            pdf_writer.add_page(page)
        else:
            if i in range(range_pages[0], range_pages[1]+1):
                page.rotate(deg)
                pdf_writer.add_page(page)
            else:
                pdf_writer.add_page(page)
        i += 1

    # Save the rotated PDF file to a BytesIO object
    output = BytesIO()
    pdf_writer.write(output)
    output.seek(0)

    st.write(f"{pdf_file.name}  has been rotated clockwise by {deg} degrees.")

    return output


def count_pages(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    return len(pdf_reader.pages)


####################################################################### MAIN #######################################################################

def main():
    st.set_page_config(page_title='PDF Rotator', page_icon=':page_with_curl:')

    st.title('PDF Rotator', )

    # Input rotation angle
    deg = st.number_input('Rotation angle in degrees (clockwise)', value=90, min_value=-360, max_value=360, step=90)
    if deg == 0:
        st.warning('Please enter a non-zero rotation angle.')

    # Upload PDF file
    pdf_file = st.file_uploader('Upload your PDF file', type=['pdf'], accept_multiple_files=False)

    # Input the range of pages to rotate
    if pdf_file is not None:
        num_pages = count_pages(pdf_file)
        if num_pages > 1:
            range_pages = st.slider('Select the range of pages to rotate', min_value=1, max_value=num_pages, value=(1, num_pages))
        else:
            range_pages = None

    if st.button("Rotate PDF", ):
        with st.spinner('Rotating PDF...'):
            if pdf_file is not None:
                pdf_out = rotate_pdf(pdf_file, int(deg), range_pages)

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
