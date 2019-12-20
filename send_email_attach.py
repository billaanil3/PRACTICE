import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


SUBJECT = "Email Data"

msg = MIMEMultipart()
msg['Subject'] = SUBJECT
msg['From'] = 'billaanil3@gmail.com'
msg['To'] = 'anil.b@onedelta.in'

part = MIMEBase('application', "octet-stream")
part.set_payload(open("/home/anil/Desktop/Detailed_Reports/my_python_files.zip", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="output.zip"')

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("billaanil3@gmail.com", "Anji@123")
server.sendmail('billaanil3@gmail.com', 'anil.b@onedelta.in', msg.as_string())
