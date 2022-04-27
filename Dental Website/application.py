from flask import Flask,render_template

app =Flask(__name__)

#index
@app.route("/")
def index():
    return render_template("index.html")


#about_Us
@app.route("/About_Us")
def About_Us():
    return render_template("About_Us.html")


#contact_Us
@app.route("/Contact_Us")
def Contact_Us():
    return render_template("Contact_Us.html")


#Member
@app.route("/Member")
def Member():
    return render_template("Member.html")
