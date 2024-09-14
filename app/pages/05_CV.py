import re
import markdown as md
import streamlit as st

from io import BytesIO
from pathlib import Path
from weasyprint import HTML
from layout import header, footer
from helpers.toc import generate_toc


# ---VISUAL CUSTOMIZATION---
header()


# ---MARKDOWN MAIN CONTENT---
path = Path(__file__).parents[1].joinpath("texts")
file_name = f'cv_bogdan_sikorsky.md'
file = Path(path).joinpath(file_name)
with open(file, 'r') as f:
    markdown_content = f.read()
st.markdown(markdown_content, unsafe_allow_html=True)


# ---GENERATING TABLE OF CONTENTS---
toc_html = generate_toc(markdown_content)
st.sidebar.markdown(toc_html, unsafe_allow_html=True)


# ---CONTACTS---
footer()