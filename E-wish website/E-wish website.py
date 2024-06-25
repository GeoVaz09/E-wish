from flask import Flask, render_template
from distutils.log import debug 
from fileinput import filename 
from flask import *  
app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   

@app.route("/wish/<wish>/<image>/<sender>/")
def wish_type(wish, image, sender):
    return render_template("wish.html", wish=wish, image=image, sender=sender)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True, port=80)