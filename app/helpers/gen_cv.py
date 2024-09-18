import markdown as md

from io import BytesIO
from pathlib import Path
from weasyprint import HTML


def convert_cv_markdown_to_pdf():
    # Open file
    path = Path(__file__).parents[1].joinpath("texts")
    file_name = f'cv_bogdan_sikorsky.md'
    file = Path(path).joinpath(file_name)
    with open(file, 'r') as f:
        markdown_text = f.read()
    html_text = md.markdown(markdown_text)

    # Define CSS for sans-serif font
    css = """
    <style>
        body {
            font-family: Calibri, sans-serif;
        }
    </style>
    """
    # Combine CSS with the HTML content
    html_with_css = f"{css}{html_text}"
    # html_with_css = html_text  #test

    # Convert markdown to HTML and generating pdf
    pdf_buffer = BytesIO()
    HTML(string=html_with_css).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer
