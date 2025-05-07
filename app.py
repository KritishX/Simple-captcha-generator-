from flask import Flask, render_template, request, session, redirect, url_for, send_file
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import io
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

# Path to TTF font in this case i choosed dejavu font
FONT_PATH = os.path.join('static', 'fonts', 'DejaVuSans-Bold.ttf')

def generate_captcha_text(length=5):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_color():
    return (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

def generate_captcha_image(text):
    width, height = 250, 90
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Loading the downloaded TTF font
    try:
        font = ImageFont.truetype(FONT_PATH, 48)
    except IOError:
        font = ImageFont.load_default()

    # Calculate spacing of text
    spacing = width // len(text)

    # Drawing each character with random position and color
    for i, char in enumerate(text):
        x = spacing * i + random.randint(5, 15)
        y = random.randint(5, 25)
        angle = random.randint(-25, 25)

        # Creating single character image to rotate
        char_image = Image.new('RGBA', (60, 60), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((5, 5), char, font=font, fill=random_color())
        rotated_char = char_image.rotate(angle, expand=1)

        image.paste(rotated_char, (x, y), rotated_char)

    # Add noise to cover the letter so cant be viewed easily at a glance (lines)
    for _ in range(6):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill=random_color(), width=2)

    # Add noise to cover the letter so cant be viewed easily at a glance (dots)
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=random_color())

    # Slight blur for smoothness
    image = image.filter(ImageFilter.SMOOTH)

    return image

@app.route('/')
def index():
    captcha_text = generate_captcha_text()
    session['captcha_text'] = captcha_text
    return render_template('index.html')

@app.route('/captcha_image')
def captcha_image():
    captcha_text = session.get('captcha_text', '')
    image = generate_captcha_image(captcha_text)

    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

@app.route('/verify', methods=['POST'])
def verify():
    user_input = request.form.get('captcha_input', '').strip().upper()
    actual_captcha = session.get('captcha_text')

    if user_input == actual_captcha:
        return '<h2 style="color:green;">CAPTCHA verified successfully!</h2><a href="/">Try again</a>'
    else:
        return '<h2 style="color:red;">Incorrect CAPTCHA. Try again!!!</h2><a href="/">Back</a>'

if __name__ == '__main__':
    app.run(debug=True)
