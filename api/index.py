from flask import Flask, request, render_template, redirect, url_for, flash
import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'  # Change this if using another service
SMTP_PORT = 587
SMTP_USER = os.getenv('SMTP_USER')  # Replace with your email
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')  # Replace with your app-specific password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Validate email addresses
        email_list = request.form.get('emails').split(',')
        valid_emails = [email.strip() for email in email_list if validate_email(email.strip())]

        if not valid_emails:
            flash('No valid email addresses provided')
            return redirect(request.url)

        for email in valid_emails:
            try:
                send_email_with_attachment(email, file.filename, filepath)
                flash(f'Email successfully sent to {email}')
            except Exception as e:
                flash(f'Error sending email to {email}: {str(e)}')
                continue

        flash('File processing completed.')
        return redirect(url_for('index'))

def send_email_with_attachment(to_email, filename, filepath):
    # Create an EmailMessage object and set it as multipart
    msg = EmailMessage()
    msg['From'] = formataddr(('Your Name', SMTP_USER))
    msg['To'] = to_email
    msg['Subject'] = 'Here is your file'
    msg.set_content('Please find the attached file.')

    # Attach the file
    try:
        print(f"Reading file: {filepath}")
        with open(filepath, 'rb') as f:
            mime = MIMEBase('application', 'octet-stream')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            mime.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            # Correctly set the email message as multipart before attaching
            msg.add_attachment(mime.get_payload(decode=True), maintype='application', subtype='octet-stream', filename=filename)
        print(f"File {filename} attached successfully.")

        # Send the email via SMTP server
        print(f"Connecting to SMTP server {SMTP_SERVER}:{SMTP_PORT}")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Error during email sending process: {str(e)}")  # Detailed error print
        raise e

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
