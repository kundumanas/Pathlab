from flask import Flask ,render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/feature")
def feature():
    return render_template('feature.html')

@app.route("/appointment")
def appointment():
    return render_template('appoinment.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')
