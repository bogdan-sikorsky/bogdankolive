import string
import random

from PIL import Image, ImageDraw, ImageFont


# Function to generate a CAPTCHA image
def generate_captcha():
    width, height = 180, 60
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=36)

    # Generate random text
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Draw text on image
    draw.text((10, 5), text, font=font, fill=(0, 0, 0))

    return image, text