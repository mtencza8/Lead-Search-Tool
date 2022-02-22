from distutils.log import error
import smtplib
from email.message import EmailMessage
import simple_salesforce as ssf




def sendEmail(fname, email):
    try:

        user="mtencza@ueidaq.com"
        password = '3Rusf0608'
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
        smtpserver.login(user, password)
        smtpserver.send_message (msg)
        smtpserver.close()
        
    except:
        print("There was some other error")









