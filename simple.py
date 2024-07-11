import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Step 2: Set Email Credentials
sender_address = 'XXXXXXXX@gmail.com'
sender_pass = 'XXXXXXXXXXXX'
receiver_address = 'XXXXXXXX@gmail.com'

# Step 3: Create SMTP Session
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Use 587 for TLS
smtp_server.starttls()

# Step 4: Log In to SMTP Server
smtp_server.login(sender_address, sender_pass)

# Step 5: Compose Email
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Test Email from Python'  # Subject of the email
body = 'This is a test email sent from Python using Gmail SMTP.'  # Email body
message.attach(MIMEText(body, 'plain'))

# Step 6: Send Email
text = message.as_string()
smtp_server.sendmail(sender_address, receiver_address, text)

# Step 7: Terminate SMTP Session
smtp_server.quit()

print("Email has been sent successfully.")
