import os
import streamlit as st

from pathlib import Path

from helpers.contacts import prepare_contacts
from helpers.gen_cv import convert_cv_markdown_to_pdf


# ---VISUAL CUSTOMIZATION---
def header():
    # ---PAGE SETTINGS---
    st.set_page_config(
        page_title='Bogdan Sikorsky, Data Engineer',
        page_icon='https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/danko_favicon.png',
        layout="wide",
        # initial_sidebar_state="collapsed",
    )

    # ---HEADER LOGO---
    st.subheader("", divider='green')
    col1, col2, col3, col4, col5 = st.columns([1,1,2,1,1])
    col3.markdown(
        f"<img src='https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/danko_logo.png' alt='WebsiteLogo'>",
        unsafe_allow_html=True
    )
    # col3.image('/home/bogdan/Documents/git/bogdanko_live/app/logo_bogdanko_live_03.png')
    st.subheader("", divider='green')

    # ---USING CUSTOM CSS---
    # Extracting colors from Streamlit theme
    color_text = st.get_option("theme.textColor")
    color_primary = st.get_option("theme.primaryColor")
    color_background = st.get_option("theme.backgroundColor")

    path = Path(__file__).parents[0].joinpath()
    file_name = f'style/styles.css'
    file = Path(path).joinpath(file_name)
    with open(file, 'r') as f:
        custom_css = f.read().replace(
            'textColor', color_text
        ).replace(
            'primaryColor', color_primary
        ).replace(
            'backgroundColor', color_background
        )  # replacing variables with colours
        st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)



# ---CONTACTS---
def footer():
    # Sidebar
    st.sidebar.download_button(
        label="Download  CV",
        data=convert_cv_markdown_to_pdf(),  # Generate PDF
        file_name="Bogdan_Sikorsky_CV.pdf",
        mime="application/octet-stream",
        type='primary',
        use_container_width = True,
    )
    st.sidebar.markdown(prepare_contacts(), unsafe_allow_html=True)

    # Bottom
    st.subheader("", divider='green')

    col1, col2, col3, col4, col5 = st.columns(5)
    col3.download_button(
        label="Download CV",
        data=convert_cv_markdown_to_pdf(),  # Generate PDF
        file_name="Bogdan_Sikorsky_CV.pdf",
        mime="application/octet-stream",
        type='primary',
        use_container_width=True,
    )

    col1, col2, col3, col4, col5 = st.columns(5)
    col3.markdown(prepare_contacts(), unsafe_allow_html=True)
    col5.text('© 2024 Bogdan Sikorsky')
    # col5.text(
    #     'Kyiv, Ukraine \n\n'
    #     '© 2024 Bogdan Sikorsky'
    # )

