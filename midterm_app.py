from flask import Flask, request, render_template

sample = Flask(__name__)

@sample.route("/")
def login():
  return render_template("login.html")

@sample.route("/registration.html", method=['POST'])
def register():
    return render_template("registration.html")

if __name__== "__main__":
    sample.run(host="0.0.0.0", port=5000)