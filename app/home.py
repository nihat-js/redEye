from flask import Blueprint, render_template

homeBlueprint = Blueprint("home", __name__)

@homeBlueprint.route("/")
def index():
    return render_template("home/index.html")

@homeBlueprint.route("/about")
def about():
    return render_template("home/about.html")

@homeBlueprint.route("/contact")
def contact():
    return render_template("home/contact.html")


@homeBlueprint.route("/services")
def services():
    return render_template("home/services.html")

@homeBlueprint.route("/team")
def test():
    return render_template("home/team.html")



@homeBlueprint.route("/portfolio")
def portfolio():
    return render_template("home/portfolio.html")

@homeBlueprint.route("/blog")
def blog():
    return render_template("home/blog.html")

@homeBlueprint.route("/single")
def single():
    return render_template("home/single.html")

@homeBlueprint.route("/elements")
def elements():
    return render_template("home/elements.html")
