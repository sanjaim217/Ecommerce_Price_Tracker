
from flask import Flask, render_template, request, redirect
from database import init_db, add_product, get_products
from scraper import get_price
from alert import send_email

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        target = float(request.form["target"])
        price = get_price(url)
        add_product(url, price, target)
        if price <= target:
            send_email(price, target, url)

        return redirect("/")
    products = get_products()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
