import streamlit as st

from layout import header, footer
from helpers.toc import generate_toc
from helpers.newsfeed import fetch_medium_articles


# ---VISUAL CUSTOMIZATION---
header()


# ---MARKDOWN MAIN CONTENT---
markdown_content = fetch_medium_articles()
st.markdown(markdown_content, unsafe_allow_html=True)


# ---GENERATING TABLE OF CONTENTS---
toc_html = generate_toc(markdown_content)
st.sidebar.markdown(toc_html, unsafe_allow_html=True)


# ---CONTACTS---
footer()
