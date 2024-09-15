import streamlit as st
from pathlib import Path

from layout import header, footer


# ---VISUAL CUSTOMIZATION---
header()


# ---MARKDOWN MAIN CONTENT---
path = Path(__file__).parents[1].joinpath("texts")
file_name = f'about_website.md'
file = Path(path).joinpath(file_name)
with open(file, 'r') as f:
    markdown_content = f.read()
st.markdown(markdown_content, unsafe_allow_html=True)


# ---CONTACTS---
footer()
