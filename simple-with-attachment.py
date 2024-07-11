import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Step 2: Set Email Credentials and Info
from_email = 'XXXXXXXX@gmail.com'
password = 'XXXXXXXXXXXX'
to_email = 'XXXXXXXX@gmail.com'


# Step 3: Create MIME Multipart Email
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = "Test Email with Attachment"

# Step 4: Attach Body to Email
body = "This is a test email sent from Python with an attachment."
msg.attach(MIMEText(body, 'plain'))

# Step 5: Attach File to Email
filename = "attachment.txt"  # Specify the filename here
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# Step 6: Set SMTP Server and Port
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Step 7: Log In and Send Email
server.login(from_email, password)
text = msg.as_string()
server.sendmail(from_email, to_email, text)

# Step 8: Close SMTP Session
server.quit()

print("Email with attachment sent successfully.")
