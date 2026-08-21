from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "change-this-secret-key"
)

PRODUCTS = {
    "15days": {
        "name": "15 Days Auto Like",
        "days": 15,
        "likes": 3300,
        "price": 120
    },
    "30days": {
        "name": "30 Days Auto Like",
        "days": 30,
        "likes": 6600,
        "price": 200
    },
    "60days": {
        "name": "60 Days Auto Like",
        "days": 60,
        "likes": 13200,
        "price": 350
    },
    "120days": {
        "name": "120 Days Auto Like",
        "days": 120,
        "likes": 26400,
        "price": 750
    },
    "180days": {
        "name": "180 Days Auto Like",
        "days": 180,
        "likes": 39600,
        "price": 1100
    },
    "365days": {
        "name": "365 Days Auto Like",
        "days": 365,
        "likes": 80300,
        "price": 2100
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shop")
def shop():
    return render_template(
        "shop.html",
        products=PRODUCTS
    )


@app.route("/checkout")
def checkout():
    plan = request.args.get("plan")

    if not plan or plan not in PRODUCTS:
        return "Invalid plan", 400

    return render_template(
        "checkout.html",
        product=PRODUCTS[plan],
        plan=plan
    )


@app.route("/order", methods=["POST"])
def order():
    uid = request.form.get("uid", "").strip()
    region = request.form.get("region", "").strip()
    plan = request.form.get("plan", "").strip()
    name = request.form.get("name", "").strip()

    if not uid:
        return "UID is required", 400

    if not region:
        return "Region is required", 400

    if not name:
        return "Name is required", 400

    if not plan or plan not in PRODUCTS:
        return "Invalid plan", 400

    product = PRODUCTS[plan]

    flash(f"✅ Order placed! UID: {uid}")

    return render_template(
        "success.html",
        uid=uid,
        region=region,
        plan=product
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
