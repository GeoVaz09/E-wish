from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return render_template("index.html")


@app.route("/<wish>")
def wish_type(wish):
    return render_template("wish.html", wish=wish)


if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True, port=80)