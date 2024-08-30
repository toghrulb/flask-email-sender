from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask on Vercel!'

# Add your other routes and functions here

if __name__ == "__main__":
    app.run(debug=True)
