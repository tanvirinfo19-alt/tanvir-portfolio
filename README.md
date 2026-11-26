# Tanvir Rahman — Python Flask Portfolio

## Requirements
- Python 3.10+
- pip

## Run locally

```bash
# 1. Open this project folder in VS Code terminal
# 2. Create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the website
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Customize before publishing
Edit `PROFILE`, `SKILLS`, and `PROJECTS` in `app.py`.
Replace the placeholder email, GitHub and LinkedIn links.
Update the education status to reflect your current situation.
Put your CV PDF in `static/files/` and add a Resume link in `templates/index.html` if needed.

## Contact form note
The demo contact form prints messages in the Flask terminal. It does not send email yet.
Connect an email provider or database before using it in production.

## Production note
Do not deploy with `debug=True`. Use a production WSGI server and set a strong `SECRET_KEY`.
