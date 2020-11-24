from flask import Flask, jsonify
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ 'roll': randint(1, 6) })
