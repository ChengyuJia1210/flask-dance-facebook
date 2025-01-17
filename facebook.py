import os
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["FACEBOOK_OAUTH_CLIENT_ID"] = os.environ.get("FACEBOOK_OAUTH_CLIENT_ID")
app.config["FACEBOOK_OAUTH_CLIENT_SECRET"] = os.environ.get("FACEBOOK_OAUTH_CLIENT_SECRET")
facebook_bp = make_facebook_blueprint()
app.register_blueprint(facebook_bp, url_prefix="/login")

@app.route("/")
def index():
    if not facebook.authorized:
        print("Try to OAuth login :", facebook.authorized)
        return redirect(url_for("facebook.login"))
    print("Authorized already")
    resp = facebook.get("/me")
    assert resp.ok, resp.text
    #return "You are {name} on Facebook, more detail{detail}".format(name=resp.json()["name"], detail=resp.json())
    return render_template('h1.html')
