Project Title: Python CAPTCHA Generator using Flask
Project Description
This project is a web-based CAPTCHA generator built using Python Flask and Pillow (PIL) libraries. The primary goal of the application is to generate a dynamic and secure CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) to protect web forms from automated submissions and bots.

The application displays a randomly generated CAPTCHA image containing a mixture of uppercase letters and digits, with visual distortions and noise to prevent automated recognition by OCR (Optical Character Recognition) systems. The user is prompted to enter the text displayed in the CAPTCHA image to verify that they are human.

Key Features
Randomized CAPTCHA text using uppercase letters and digits

Stylish and readable font with random angles and positions for each character

Visual noise including lines and dots for added security

User-friendly interface with a modern, responsive, and clean design

Session-based verification — the CAPTCHA text is securely stored in server session for validation

Immediate feedback — users are notified whether the entered CAPTCHA is correct or incorrect

Tools & Technologies
Backend: Python, Flask

Frontend: HTML5, CSS3

Image Generation: Pillow (PIL)

Font Rendering: Custom TTF font (DejaVuSans-Bold.ttf)

Workflow
On visiting the main page (/), the server generates a random CAPTCHA text and stores it in the session.

A corresponding CAPTCHA image is dynamically generated using Pillow and displayed on the page.

The user enters the text they see in the image into the input field and submits the form.

The server verifies whether the user’s input matches the stored CAPTCHA text.

The application responds with a success or failure message.

Applications
Form validation for contact forms, registration, and login pages

Protection against automated spam bots and brute-force attacks

Educational demonstration of image generation and web application security

Dependencies
Python 3.x

Flask

Pillow (PIL)

How to Run
bash
Copy
Edit
pip install flask pillow
python app.py
Visit http://127.0.0.1:5000/ in your web browser.

