CONTACTS = [
    (
        'Bogdan',
        'https://bit.ly/Website_Bogdan_Sikorsky',
        'https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/_social%20(1).png',
    ),
    (
        'Gmail',
        'mailto:bogdan.sikorsky.dev@gmail.com',
        'https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/_email%20(1).png',
    ),
    (
        'LinkedIn',
        'https://bit.ly/LinkedIn_Bogdan_sikorsky',
        'https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/_linkedin%20(1).png',
    ),
    (
        'UpWork',
        'https://bit.ly/UpWork_Bogdan_Sikorsky',
        'https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/_upwork%20(1).png',
    ),
    (
        'GitHub',
        'https://bit.ly/GitHub_Bogdan_Sikorsky',
        'https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/_github%20(1).png',
    ),
    (
        'YouTube',
        'https://bit.ly/YouTube_Bogdan_Sikorsky',
        'https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/black/_youtube%20(1).png',
    ),
]

def prepare_contacts():
    res = []
    for item in CONTACTS:
        name, link, img_src = item
        res.append(f'<a href="{link}" class="contact-item"><img src="{img_src}" alt="{name}" width="30" height="30"></a>')
    result = f'''
        <div class="contacts-container">
            {"".join(res)}
        </div>
    '''
    return result