from flask import Flask, render_template
from monitor import ping, get_wifi_signal
import os
import pymysql
from pathlib import Path
from dotenv import load_dotenv
from secrets import token_urlsafe
from flask import request
from werkzeug.security import check_password_hash
from flask import Flask, abort, redirect, render_template, request, session, url_for
app = Flask(__name__)

load_dotenv(Path(__file__).with_name(".env"))
app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]

@app.route("/Monitor")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    wifi_signal, wifi_name = get_wifi_signal()
    return render_template(
        "index.html",
        ping=ping,
        wifi_signal=wifi_signal,
        wifi_name=wifi_name,
    )

@app.route("/Test")
def test():
  return '''<script> setTimeout(function(){
   window.location.reload(1);
}, 1000); console.log(Date.now())</script>'''

@app.route("/admin")
def kontakt():
  return render_template("admin.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    token = session.setdefault("login_token", token_urlsafe(32))
    error = None

    if request.method == "POST":
        if request.form.get("token") != token:
            abort(400)

        with pymysql.connect(
            unix_socket="/run/mysqld/mysqld.sock",
            user="monitor_app",
            password=os.environ["MONITOR_DB_PASSWORD"],
            database="pi_monitor",
        ) as db:
            with db.cursor() as cursor:
                cursor.execute(
                    "SELECT id, password_hash FROM users WHERE username = %s",
                    (request.form.get("username", "").strip(),),
                )
                user = cursor.fetchone()

        if user and check_password_hash(user[1], request.form.get("password", "")):
            session.clear()
            session["user_id"] = user[0]
            return redirect(url_for("index"))

        error = "Feil brukernavn eller passord."

    return render_template("login.html", token=token, error=error)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
