import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ritav'
email['to'] = 'Ritavdas@gmail.com'
email['subject'] = 'You won ₹1,000,000'

email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ritavdas2020@gmail.com', 'ritav07022000')  # Enter your email address and password
    smtp.send_message(email)
    print("All Good! ")
