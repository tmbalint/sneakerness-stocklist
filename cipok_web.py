from flask import Flask, render_template, send_file, request, jsonify
import qrcode
from io import BytesIO

app = Flask(__name__)

# Sample data for your shoes
shoes = [
  {"name": "Balenciaga Track Bordeaux", "image": "balenci-track-bordeaux.png", "size": "42", "condition": "USED 10/9, OG NONE", "price": "115 000 Ft - 300 €"},
  {"name": "Balenciaga Track Orange/Blue", "image": "balenci-track-orange-blue.png", "size": "42", "condition": "USED 10/8, OG NONE", "price": "105 000 Ft - 275 €"},
  {"name": "Balenciaga Track White", "image": "balenci-track-white.webp", "size": "42", "condition": "USED 10/9, OG NONE", "price": "125 000 Ft - 325 €"},
  {"name": "Dior B23 Oblique Black", "image": "dior-b23-oblique-black.webp", "size": "42", "condition": "USED 10/9, OG NONE", "price": "115 000 Ft - 300 €"},
  {"name": "Jordan 1 High Mocha", "image": "jordan1-high-mocha.webp", "size": "44.5", "condition": "USED 10/9, BOX", "price": "55 000 Ft - 145 €"},
  {"name": "Jordan 1 High Mocha", "image": "jordan1-high-mocha.webp", "size": "42.5", "condition": "USED 10/7-8, OG NONE", "price": "40 000 Ft - 105 €"},
  {"name": "Jordan 1 Stage Haze", "image": "air-jordan-1-retro-high-og-stage-haze-1-1000.webp", "size": "42", "condition": "USED 10/9+, OG NONE", "price": "45 000 Ft - 120 €"},
  {"name": "Jordan 1 TS Canary", "image": "travis-canary.webp", "size": "42", "condition": "DS WITH FLAW, OG ALL", "price": "125 000 Ft - 325 €"},
  {"name": "Jordan 1 TS Medium Olive", "image": "medium-olive.webp", "size": "42.5", "condition": "USED 10/8+, OG NONE", "price": "145 000 Ft - 375 €"},
  {"name": "Jordan 1 TS Medium Olive", "image": "medium-olive.webp", "size": "41, 42, 42.5, 43", "condition": "DS, OG ALL", "price": "210 000 Ft - 545 €"},
  {"name": "Jordan 4 A Ma Maniére", "image": "j4-a-ma-maniere.webp", "size": "42", "condition": "DS, OG ALL EXCEPT EXTRA BOX", "price": "85 000 Ft - 220 €"},
  {"name": "Jordan 4 Fire Red", "image": "j4-fire-red.webp", "size": "43", "condition": "USED 10/8+, OG NONE", "price": "40 000 Ft - 105 €"},
  {"name": "Jordan 4 Oreo", "image": "air-jordan-4-retro-white-oreo-2021-1-1000.webp", "size": "44", "condition": "USED 10/9, OG NONE", "price": "60 000 Ft - 155 €"},
  {"name": "Jordan 4 Oreo", "image": "air-jordan-4-retro-white-oreo-2021-1-1000.webp", "size": "45", "condition": "USED 10/9, BOX", "price": "65 000 Ft - 170 €"},
  {"name": "Jordan 4 SB Pine Green", "image": "j4-sb-pine-green.webp", "size": "42", "condition": "USED 10/9+, OG NONE", "price": "95 000 Ft - 245 €"},
  {"name": "New Balance 2002R", "image": "nb-2002r.webp", "size": "44", "condition": "USED 10/8+, OG NONE", "price": "30 000 Ft - 80 €"},
  {"name": "Nike Dunk Low Lot 33", "image": "ow-lot33.webp", "size": "42", "condition": "USED 10/9+, OG ALL", "price": "75 000 Ft - 195 €"},
  {"name": "Nike SB Dunk Low Wizard Oz", "image": "FZ1291-600-sb-poppyfield-side.webp", "size": "45", "condition": "DS, OG ALL", "price": "45 000 Ft - 120 €"},
  {"name": "Off-White Dunk Low Lot 28", "image": "ow-lot28.webp", "size": "42", "condition": "USED 10/9, ONE FLAW, OG ALL", "price": "60 000 Ft - 155 €"},
  {"name": "SB Dunk Lobster Orange", "image": "concepts-x-nike-dunk-sb-low-orange-lobster-1-1000.webp", "size": "44", "condition": "USED 10/9, OG ALL", "price": "130 000 Ft - 335 €"},
  {"name": "Yeezy Foam", "image": "foam-cinder.webp", "size": "43", "condition": "USED 10/9, OG ALL", "price": "30 000 Ft - 80 €"},
  {"name": "Travis Scott AF1 Sail", "image": "travisaf.jpg", "size": "41", "condition": "USED 10/9, OG ALL", "price": "115 000 Ft - 300 €"},
  {"name": "VLONE Butterfly Tee", "image": "vlone.webp", "size": "XL", "condition": "DS, OG NONE", "price": "25 000 Ft - 65 €"},
  {"name": "Yeezy Boost Static", "image": "yeezystatic.webp", "size": "43", "condition": "USED 10/7, OG NONE", "price": "20 000 Ft - 55 €"},
  {"name": "Yeezy Boost Tail Light", "image": "yeezytaillight.jpeg", "size": "44", "condition": "USED 10/8, OG ALL", "price": "30 000 Ft - 80 €"},
  {"name": "Jordan 4 SB Navy", "image": "j4navy.webp", "size": "46, 43", "condition": "DS, OG ALL", "price": "85 000 Ft - 220 €"}
]

@app.route("/")
def index():
    return render_template("index.html", shoes=shoes)

@app.route("/filter")
def filter_shoes():
    """API endpoint for filtering shoes"""
    conditions = request.args.getlist('condition')
    
    filtered_shoes = shoes
    
    if conditions:
        filtered_shoes = []
        for shoe in shoes:
            for condition in conditions:
                if condition == "Used" and "USED" in shoe["condition"]:
                    filtered_shoes.append(shoe)
                    break
                elif condition == "DS" and shoe["condition"].startswith("DS"):
                    filtered_shoes.append(shoe)
                    break
    
    return jsonify(filtered_shoes)

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