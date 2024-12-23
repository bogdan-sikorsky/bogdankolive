import streamlit as st

from io import BytesIO
from pathlib import Path
from layout import header, footer
from email_validator import validate_email, EmailNotValidError

from helpers.mailing import send_email
from helpers.captcha import generate_captcha


# ---VISUAL CUSTOMIZATION---
header()


# ---MARKDOWN MAIN CONTENT---
path = Path(__file__).parents[1].joinpath("texts")
file_name = f'contacts_bogdan_sikorsky.md'
file = Path(path).joinpath(file_name)
with open(file, 'r') as f:
    markdown_text = f.read()
st.markdown(markdown_text, unsafe_allow_html=True)


# ---CONTACT FORM---
# Function to regenerate CAPTCHA and update image
def regenerate_captcha(image_placeholder = None):
    st.session_state.captcha_image, st.session_state.captcha_text = generate_captcha()

    # Store CAPTCHA image in buffer
    st.session_state.captcha_buffer = BytesIO()
    st.session_state.captcha_image.save(st.session_state.captcha_buffer, format="PNG")
    st.session_state.captcha_buffer.seek(0)

    # reloads image on front-end if validation failed
    try:
        image_placeholder.image(st.session_state.captcha_buffer, use_column_width=False)
    except:
        pass


# Initialize session state for CAPTCHA if not already done
if 'captcha_text' not in st.session_state:
    regenerate_captcha()


# Form view
with st.form(key='contact_form'):

    # General fields
    name = st.text_input(
        'Name', max_chars=50, placeholder='Enter your name here'
    )
    email = st.text_input(
        'Email', max_chars=50, placeholder='Enter your email here'
    )
    msg_subject = st.text_input(
        'Subject', max_chars=50, placeholder='Enter subject of your message here'
    )
    message = st.text_area(
        'Message', max_chars=2000, placeholder='Enter your message here'
    )

    # Captcha image and input
    st.markdown('Ensure that browser settings do not block CAPTCHA image rendering')
    column_image, column_answer = st.columns([1, 1])
    image_placeholder = column_image.empty()
    image_placeholder.image(st.session_state.captcha_buffer, use_column_width=False)
    captcha_response = column_answer.text_input(
        'CAPTCHA', max_chars=6, placeholder='Enter CAPTCHA here'
    )

    # Confirm button
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col3:
        submit_button = st.form_submit_button('Send', use_container_width=True)

    # Checks and sending
    if submit_button:

        # Validate the email address
        try:
            validate_email(email)

            # Captcha validation
            if captcha_response == st.session_state.captcha_text:

                # Send email
                email_body = f"Name:\n{name}\n\nEmail:\n{email}\n\nSubject:\n{msg_subject}\n\nMessage:\n{message}"
                send_email('My Contact Form: ' + msg_subject, email_body)
                st.success('Message sent successfully!')
            else:
                st.error('CAPTCHA verification failed. Please try again.')

            # Regenerate the CAPTCHA after a failed attempt
            regenerate_captcha(image_placeholder)

        except EmailNotValidError as e:
            st.error(f"Invalid email address: {e}")

            # Regenerate the CAPTCHA after a failed email validation
            regenerate_captcha(image_placeholder)

# ---CONTACTS---
footer()
