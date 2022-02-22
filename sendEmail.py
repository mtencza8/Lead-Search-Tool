from distutils.log import error
import smtplib
from email.message import EmailMessage
import simple_salesforce as ssf


with open("info.config") as f:
    contents = f.readlines()

for i in contents:
    print(i)
    if "username" in i:
        username = i
        index = username.index(":")
        username = username[index+1:].strip()
    if "password" in i:
        password = i
        index = password.index(":")
        password = password[index+1:].strip()







def sendEmail(fname, email):
    try:

        smtpsrv = "smtp.office365.com"
        smtpserver = smtplib.SMTP(smtpsrv,587)
        msg = EmailMessage()

        msg['Subject'] = 'Setting up a meeting?'
        msg['From'] = 'mtencza@ueidaq.com'
        msg['To'] = email
        body = msg.set_content("""\
            {}:

            I'd love to introduce you to UEI.  We make rugged, reliable and flexible data acquisition hardware.

            Mike Tencza
            """
        ).format(fname)

        smtpserver.starttls()
        smtpserver.login(username, password)
        smtpserver.send_message (msg)
        smtpserver.close()
        
    except:
        print("There was some other error")









