# Flask Email Sender

Flask Email Sender is a web application that allows users to upload files and send them as email attachments to specified recipients. This app uses Flask as the backend framework and SMTP for sending emails, making it simple and effective for handling file uploads and email communication.

## Features

- Upload files and send them to multiple email addresses.
- Validates email addresses to ensure they are correctly formatted.
- Sends emails securely using SMTP (Gmail, Outlook, etc.).

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- An SMTP server (e.g., Gmail, Outlook)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-email-sender.git
   cd flask-email-sender
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

4. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Set up environment variables:

- Create a .env file in the root of your project with the following:
   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your_email@gmail.com
   SMTP_PASSWORD=your_app_password  # Use an App Password for Gmail

5. Run the application:
   ```bash
   flask run

### Usage

 1. Open your browser and go to http://127.0.0.1:5000.
 2. Upload a file and enter comma-separated email addresses.
 3. Click the "Upload and Send" button to send the file to the specified recipients.

### Environment Variables

> | Variable        | Description                                     |
> |-----------------|-------------------------------------------------|
> | `SMTP_SERVER`   | The SMTP server address (e.g., `smtp.gmail.com`)|
> | `SMTP_PORT`     | The SMTP server port (usually `587` for TLS)    |
> | `SMTP_USER`     | Your email address used to send emails          |
> | `SMTP_PASSWORD` | Your SMTP or App-specific password              |






### Key Points:
- This README focuses on local setup and running instructions.
- Ensure you replace placeholders with your actual information.
- The `.env` setup helps manage sensitive credentials securely without hardcoding them in your source code.

Let me know if you need any other modifications!
