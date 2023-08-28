from flask import Flask, render_template, request
import qrcode
import os
import random
import string

app = Flask(__name__)


def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="blue")

    random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.png'
    img_path = os.path.join('static', random_filename)
    img.save(img_path)

    return img_path


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if url:
        qr_code_path = generate_qr_code(url)
        return render_template('index.html', qr_code=qr_code_path)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
