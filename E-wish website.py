from flask import Flask, render_template
from distutils.log import debug 
from fileinput import filename 
from flask import *  
app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f"static/{f.filename}")   
        return render_template("Acknowledgement.html", name = f.filename)   


@app.route("/wish/<wish>/<image>")
def wish_type(wish, image):
    return render_template("wish.html", wish=wish, image=f"/static/{image}")


if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True, port=80)