import smtplib
from email.mime.text import MIMEText

def send_email(current_price, target_price, product_url):
    try:
        sender = "sample.sender@gmail.com"      # REAL Gmail ID
        password = "abcd efgh ijkl mnop"         # REAL App Password
        receiver = "tech@gmail.com"              # Receiver email

        subject = "Price Drop Alert 🚨"
        body = f"""
Hello Tech Team,

The product price has dropped.

Current Price : {current_price}
Target Price  : {target_price}
Product URL   : {product_url}

Regards,
E-Commerce Price Tracker
"""

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)

        print("✅ Email sent successfully to tech@gmail.com")

    except Exception as e:
        print("❌ Email sending failed:", e)
