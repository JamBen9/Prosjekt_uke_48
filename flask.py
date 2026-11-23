from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hei, Flask!"
  

@app.route("/monitorering")
def om_meg():
    return render_template("index.html")

@app.route("/admin")
def kontakt():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)