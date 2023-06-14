import fitz

def replace_black_with_white(input_pdf_path, output_pdf_path):
    # Open the input PDF
    pdf = fitz.open(input_pdf_path)

    # Iterate through each page of the PDF
    for page_num in range(pdf.page_count):
        page = pdf.load_page(page_num)

        # Get the list of all objects on the page
        page_objects = page.get_drawings()

        # Iterate through each object on the page
        for obj in page_objects:
            if obj["type"] == 1:  # Check if it's a path object
                print('done')
                # Check the fill color
                if obj["fill"] == (0, 0, 0):
                    obj["fill"] = (1, 1, 1)
                # Check the stroke color
                if obj["stroke"] == (0, 0, 0):
                    obj["stroke"] = (1, 1, 1)

    # Save the modified PDF
    pdf.save(output_pdf_path)
    pdf.close()

# Usage example-


replace_black_with_white('D:\Github\Invert_pdf\input.pdf', 'D:\Github\Invert_pdf\output.pdf')
