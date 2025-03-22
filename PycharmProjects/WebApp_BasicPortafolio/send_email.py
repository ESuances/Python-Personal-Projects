import smtplib
import ssl

host = "smtp.gmail.com" #This is specific for gmail accounts
port = 465  # Standard port for gmail

username= "erick.s.suances.arc@gmail.com"
password = "smcsmurfwzskbivo"

receiver = "erick.s.suances.arc@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Hello world, or should I say email :D
Hi! this is my first mail sent to myself in python.
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)