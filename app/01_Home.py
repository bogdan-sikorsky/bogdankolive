import os
import base64
import sentry_sdk
import streamlit as st

from pathlib import Path
from dotenv import load_dotenv

from layout import header, footer
from helpers.toc import generate_toc


# ---HEALTH TRACKING---
load_dotenv()
sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    enable_tracing=True,
)


# ---VISUAL CUSTOMIZATION---
header()


# ---MARKDOWN MAIN CONTENT---
path = Path(__file__).parents[0].joinpath("texts")
file_name = f'about_bogdan_sikorsky.md'
file = Path(path).joinpath(file_name)
with open(file, 'r') as f:
    markdown_text = f.read()
st.markdown(markdown_text, unsafe_allow_html=True)


# ---GENERATING TABLE OF CONTENTS---
toc_html = generate_toc(markdown_text)
st.sidebar.markdown(toc_html, unsafe_allow_html=True)


# ---CONTACTS---
footer()


# st.audio(
#     "Бумбокс - Ой У Лузі Червона Калина.mp3", format="audio/mp3",
#     loop=False, autoplay=True
# )
