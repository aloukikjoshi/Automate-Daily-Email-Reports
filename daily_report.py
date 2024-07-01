import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import secret

# Email configuration
smtp_host = 'smtp.gmail.com'  # Update with your SMTP server
smtp_port = 587  # Update with your SMTP port
smtp_user = 'themarvelvaultofficial@gmail.com'  # Update with your email address
smtp_password = secret.password

sender = 'themarvelvaultofficial@gmail.com'
receiver = 'aloukikjoshi@gmail.com'  # Update with recipient email address
subject = 'Daily Report - ' + datetime.date.today().strftime('%Y-%m-%d')

# Create the email content
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
# This is a sample of the email body. You can customize it as needed.
body = """
Hello,

Here is your daily report.

Date: {date}

1. Task Completed:
    - Task 1: Completed
    - Task 2: Completed
    - Task 3: In Progress

2. Issues Faced:
    - Issue 1: Resolved
    - Issue 2: Unresolved

3. Plan for Tomorrow:
    - Complete Task 3
    - Start Task 4

Regards,
Your Name
""".format(date=datetime.date.today().strftime('%Y-%m-%d'))
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
try:
    smtp_server = smtplib.SMTP(smtp_host, smtp_port)
    smtp_server.starttls()
    smtp_server.login(smtp_user, smtp_password)
    smtp_server.sendmail(sender, receiver, message.as_string())
    smtp_server.quit()
    print('Email sent successfully')
except Exception as e:
    print(f'Failed to send email. Error: {str(e)}')
