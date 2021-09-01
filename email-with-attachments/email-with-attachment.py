import smtplib
import glob
import os

import datetime as datetime

import emailConfig as cf

import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = cf.emailDetails['emailFrom']
emailto = cf.emailDetails['emailTo']
fileDirectory = cf.attachmentDirectory
username = cf.emailUsername
password = cf.emailPassword

def getLatestFile():
    list_of_files = glob.glob(fileDirectory + "/*.csv")  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)
    return latest_file

fileToSend = getLatestFile()
_, fileName = os.path.split(fileToSend)

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)

datetime_object = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = cf.emailDetails['emailSubject'] + datetime_object
msg.preamble = cf.emailDetails['emailPreamble'] + datetime_object

attachment.add_header("Content-Disposition", "attachment", filename=fileName)
msg.attach(attachment)

server = smtplib.SMTP(cf.smtpServer)
server.starttls()
server.login(username,password)
server.sendmail(emailfrom, emailto.split(","), msg.as_string())
server.quit()

print("Your attachment [" + fileName + "] to the recipients [" + emailto + "] has been emailed")