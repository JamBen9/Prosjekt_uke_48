from flask import Flask, render_template
from monitor import ping

app = Flask(__name__)


@app.route("/Monitor")
def index():
  return render_template("index.html", ping=ping)



@app.route("/admin")
def kontakt():
  return render_template("admin.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
