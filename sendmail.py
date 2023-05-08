import smtplib
from email.message import EmailMessage
import os

def send_email(body):
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()

        SENDER_EMAIL ='9ijarise@gmail.com'
        RECEIVER_EMAIL ='9ijarise@gmail.com'

        # the email password was set as en environment variable
        SENDER_PASSWORD = os.environ.get('email_password')

        subject = 'get list of top trending videos on youtube'
        # body = "Hi, a new update just dropped"


        # msg = EmailMessage()
        # msg.set_content({body})
        # msg['Subject'] = {subject}
        # msg['From'] = {SENDER_EMAIL}
        # msg['To'] = {RECEIVER_EMAIL}

        email_text = f""" 
        Subject: {subject}



        body: {body}
        
        """

        server_ssl.login(SENDER_EMAIL, SENDER_PASSWORD)
        # server_ssl.send_message(msg, SENDER_EMAIL, RECEIVER_EMAIL)
        # server_ssl.quit()
        server_ssl.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_text)
        server_ssl.close()
        print ("Successfully sent email")

    except Exception as e:
        print(e)


# def attach_file():
