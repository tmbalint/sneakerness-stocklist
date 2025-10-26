from flask import Flask, render_template, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# Sample data for your shoes
shoes = [
    {"name": "Balenciaga Track White", "image": "balenci-track-white.webp", "size": "EU42", "condition": "Használt - Used", "price": "$120"},
    {"name": "Balenciaga Track Orange Blue", "image": "balenci-track-orange-blue.png", "size": "EU42", "condition": "Használt - Used", "price": "$220"},
    {"name": "Balenciaga Track Bordeaux", "image": "balenci-track-bordeaux.png", "size": "EU42", "condition": "Használt - Used", "price": "$180"},
    {"name": "Dior B23 Oblique Black", "image": "dior-b23-oblique-black.webp", "size": "EU42", "condition": "Használt - Used", "price": " "},
    {"name": "Jordan 1 High Mocha ", "image": "jordan1-high-mocha.webp", "size": "EU42.5, EU44.5", "condition": "Használt - Used", "price": " "},
    {"name": "Jordan 1 High Stage Haze ", "image": "air-jordan-1-retro-high-og-stage-haze-1-1000.webp", "size": "EU42", "condition": "Használt - Used", "price": " "},
    {"name": "Jordan 1 Low Travis Scott Canary", "image": "travis-canary.webp", "size": "EU42", "condition": "Új hibával - DS w flaw", "price": " "},
    {"name": "Jordan 1 Low Travis Scott Medium Olive", "image": "medium-olive.webp", "size": "EU41, EU42, EU42.5 x2, EU43", "condition": "DS, 42.5 Használt és Új is - Used and DS too", "price": " "},
    {"name": "Nike Air Force 1 Travis Scott Sail", "image": "travisaf.jpg", "size": "EU41", "condition": "Használt - Used", "price": " "},
    {"name": "Jordan 4 SB Navy Blue", "image": "j4navy.webp", "size": "EU46 x2, EU43", "condition": "Új - DS", "price": " "},
    {"name": "Jordan 4 AMM While You We're Sleeping", "image": "j4-a-ma-maniere.webp", "size": "EU42", "condition": "Új - DS", "price": " "},
    {"name": "Jordan 4 Fire Red", "image": "j4-fire-red.webp", "size": "EU42", "condition": "Használt - Used", "price": " "},
    {"name": "Jordan 4 Oreo", "image": "air-jordan-4-retro-white-oreo-2021-1-1000.webp", "size": "EU44, EU45", "condition": "Használt - Used", "price": " "},
    {"name": "Jordan 4 SB Pine Green", "image": "j4-sb-pine-green.webp", "size": "EU42", "condition": "Használt - Used", "price": " "},
    {"name": "New Balance 2002R", "image": "nb-2002r.webp", "size": "EU44", "condition": "Használt - Used", "price": " "},
    {"name": "Nike Dunk Low Lot 33", "image": "ow-lot33.webp", "size": "EU42", "condition": "Használt - Used", "price": " "},
    {"name": "Nike Dunk Low Lot 28", "image": "ow-lot28.webp", "size": "EU42", "condition": "Használt - Used", "price": " "},
    {"name": "Nike SB Dunk Low Oz Wizard", "image": "FZ1291-600-sb-poppyfield-side.webp", "size": "EU45", "condition": "Új - DS", "price": " "},
    {"name": "Nike SB Dunk Low Orange Lobster", "image": "concepts-x-nike-dunk-sb-low-orange-lobster-1-1000.webp", "size": "EU44", "condition": "Használt - Used", "price": " "},
    {"name": "The North Face 1996 Retro Nuptse 700", "image": "1TheNorthFace1996RetroNuptse700.webp", "size": "L", "condition": "Használt - Used", "price": " "},
    {"name": "Yeezy Foam RNNR MX Cinder", "image": "foam-cinder.webp", "size": "EU43", "condition": "Használt - Used", "price": " "},
    {"name": "Yeezy Boost 350 Static", "image": "yeezystatic.webp", "size": "EU43 1/3", "condition": "Használt - Used", "price": " "},
    {"name": "Yeezy Boost 350 Tail Light", "image": "yeezytaillight.jpeg", "size": "EU44", "condition": "Használt - Used", "price": " "},
    {"name": "VLONE x 999 Juice WRLD Butterfly tee", "image": "vlone.webp", "size": "XL", "condition": "Új - DS", "price": " "},
]

@app.route("/")
def index():
    return render_template("index.html", shoes=shoes)

@app.route("/qr")
def qr_stocklist():
    url = "https://sneakerness-stocklist-1.onrender.com/"  # live stocklist URL
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)