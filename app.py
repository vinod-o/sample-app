from flask import Flask

app = Flask(__name__)

@app.route("/login")
def login():
    return "Login API"

@app.route("/payment")
def payment():
    return "Payment API"
@app.route("/cart")
def cart():
    return "Cart API"







