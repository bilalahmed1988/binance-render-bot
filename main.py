from flask import Flask, jsonify
from binance.client import Client
import os

app = Flask(__name__)

# ⚠️ Use environment variables (IMPORTANT for security)
API_KEY = os.getenv("nWxtTTxBlT4ULnLScbvFy6tYWddtdDHvkNGATIgdRtAhJGYRdsjWdSxKCk2kratL")
API_SECRET = os.getenv("iTY5dUQrw5SxW8y0ipHnK6CS7RizmtXxOR9L9MHBNWQbBhZWn1BBcxY4dvIlCzZL")

client = Client(API_KEY, API_SECRET)

@app.route("/")
def home():
    return "Binance Bot is running 🚀"

@app.route("/balance")
def balance():
    try:
        account = client.futures_account_balance()
        return jsonify(account)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()