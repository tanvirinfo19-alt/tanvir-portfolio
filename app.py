from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

PROFILE = {
    "name": "Tanvir Rahman",
    "role": "Computer Science & Technology Student",
    "tagline": "Building with Python. Exploring the future of AI.",
    "email": "your-email@example.com",  # Replace with your email
    "github": "https://github.com/yourusername",  # Replace with your GitHub URL
    "linkedin": "https://www.linkedin.com/in/yourusername/",  # Replace with your LinkedIn URL
    "location": "Cumilla, Bangladesh",
}

SKILLS = [
    ("Python", "Backend development, scripting and problem solving"),
    ("Machine Learning & AI", "Currently learning machine learning concepts and tools"),
    ("HTML & CSS", "Responsive layouts and modern website interfaces"),
    ("JavaScript", "Interactive frontend functionality"),
    ("WordPress", "Website creation and management"),
    ("Digital Marketing", "Social media marketing and digital strategies"),
]

PROJECTS = [
    {
        "number": "01",
        "title": "Python Projects",
        "description": "A collection of Python experiments, scripts and learning projects.",
        "stack": "Python · Problem Solving",
        "url": "https://github.com/yourusername"
    },
    {
        "number": "02",
        "title": "Frontend Web Projects",
        "description": "Responsive web interfaces built with HTML, CSS and JavaScript.",
        "stack": "HTML · CSS · JavaScript",
        "url": "https://github.com/yourusername"
    },
    {
        "number": "03",
        "title": "WordPress Websites",
        "description": "Website building and content management using WordPress.",
        "stack": "WordPress · Web Design",
        "url": "https://github.com/yourusername"
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        year=datetime.now().year
    )

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all fields.", "error")
        return redirect(url_for("home") + "#contact")

    # Demo behaviour: the message is printed in the terminal.
    # For production, connect an email service or save messages in a database.
    print(f"\nNew portfolio message\nFrom: {name} <{email}>\nMessage: {message}\n")
    flash("Thanks! Your message was received by the demo form.", "success")
    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)
