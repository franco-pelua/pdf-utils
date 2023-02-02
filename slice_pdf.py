import PyPDF2

try:
    # Path in your machine that points to the file that you want to crop
    file_to_crop_path = ""

    # Desired file output name
    output_name = ""

    with open(file_to_crop_path, 'rb') as file:
        input_pdf = PyPDF2.PdfReader(file)
        output_pdf = PyPDF2.PdfWriter()

        for page_num in range(len(input_pdf.pages)):
            page = input_pdf.pages[page_num]

            width = page.mediabox.width
            height = page.mediabox.height
            
            # This settings crops and stores the first horizontal half of the page. Change accordingly.
            trim_box = PyPDF2.generic.RectangleObject([0, height/2, height, height])
            page.cropbox = trim_box

            output_pdf.add_page(page)

        with open(output_name, 'wb') as output_file:
            output_pdf.write(output_file)
        


except Exception as e:
    print(e)
