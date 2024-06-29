from flask import Flask, render_template, request, jsonify
from distutils.log import debug 
from fileinput import filename 
from flask import *
import random
import string
import os

app = Flask(__name__)   

STORAGE_FILE = 'url_codes.txt'

def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def save_url_code(url, code):
    with open(STORAGE_FILE, 'a') as f:
        f.write(f"{code},{url}\n")

def get_url_by_code(code):
    if not os.path.exists(STORAGE_FILE):
        return None
    with open(STORAGE_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            saved_code, saved_url = line.strip().split(',')
            if saved_code == code:
                return saved_url
    return None
  
@app.route('/')   
def main():   
    return render_template("index.html")   

@app.route("/wish/<sender>/<wish>/<image>/")
def wish_type(wish, image, sender):
    return render_template("wish.html", sender=sender, wish=wish, image=image)

@app.route('/post_url', methods=['POST'])
def post_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    code = generate_code()
    save_url_code(url, code)
    return jsonify({"message": "URL saved", "code": code})

@app.route('/get_url/<code>', methods=['GET'])
def get_url(code):
    url = get_url_by_code(code)
    if url:
        return jsonify({"url": url})
    else:
        return jsonify({"error": "Code not found"}), 404

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True, port=80)