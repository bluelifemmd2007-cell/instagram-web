from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    profile_pic_url = None

    if request.method == "POST":
        username = request.form["username"]
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        profile_pic_url = profile.profile_pic_url

    return render_template("index.html", profile_pic_url=profile_pic_url)

if __name__ == "__main__":
    app.run(debug=True)
