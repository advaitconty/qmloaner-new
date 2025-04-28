import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import secret as secrets


def send_email(subject, body, to_emails, attachment_path, attach=True):
    # SMTP server configuration for outlook/hotmail
    smtp_server = secrets.SMTP_SERVER
    smtp_port = secrets.SMTP_PORT
    sender_email = secrets.EMAIL_ID
    sender_password = secrets.EMAIL_PASSWORD

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        if attach:
            # Attach the PDF file
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'pdf')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                        f'attachment; filename="{attachment_path}"')
            msg.attach(part)

        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, to_emails, text)
        server.quit()

        print(f"Email sent to your email and the teachers' emails.")

    except smtplib.SMTPAuthenticationError as e:
        print(f'Authentication error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    send_email("soote", "soote", ['advait_contractor@outlook.sg'], "soote", attach=False)