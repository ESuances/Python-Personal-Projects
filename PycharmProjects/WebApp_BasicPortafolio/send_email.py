import smtplib
import ssl

def sendEmail(message):
    host = "smtp.gmail.com"  # This is specific for gmail accounts
    port = 465  # Standard port for gmail
    username = "erick.s.suances.arc@gmail.com"
    password = "smcsmurfwzskbivo"
    receiver = "erick.s.suances.arc@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
