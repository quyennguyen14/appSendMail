import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def smtpSendEmail(host, sender_email, sender_password, receiver_email, subject, html_body):

    message = MIMEMultipart("alternative")
    message["Subject"] =  subject
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_email)
    mimeType = MIMEText(html_body, "html")
    message.attach(mimeType)

    with smtplib.SMTP(host=host) as server:
        server.login(sender_email, sender_password)
        # server.send_message(
        #     sender_email, receiver_email, message.as_string()
        # )

        server.send_message(
            msg=message, from_addr=sender_email, to_addrs=receiver_email
        )

