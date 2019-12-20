# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("billaanil3@gmail.com", "Anji@123")

# message to be sent
message = "Dabba Arun"

# sending the mail
s.sendmail("billaanil3@gmail.com", "anil.b@onedelta.in", message)

# terminating the session
s.quit()
