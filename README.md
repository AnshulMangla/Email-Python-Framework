# Email-Python-Framework

# Description
This Email Python Framework allows the user to email attachments to the configured recipients. 
The framework picks the latest file of a .csv type from a pre-configured folder and emails that to a set of pre-configured recipients.
The set of recipients, attachement folder, smtp server, smtup user-password can be configured in the Configuration file.

# Installation

## Environment

Required

* Python 3.9 (and above)
* Python modules mentioned in the requirements.txt file

## Downloading

If you have git installed, clone the repository

    $ git clone https://github.com/AnshulMangla/Email-Python-Framework.git
    
## Installing & Configuration

After downloading, update the configuration file (emailConfig.py) with the following details

     $ cd email-with-attachments
    
Make the following changes to the emailConfig.py:
    
     - emailDetails.emailFrom: email id of the sender e.g. 'sender@sender.com',
     - emailDetails.emailTo: email id of the recipients (comma separated with no space for multiple e.g. 'reciever1@reciever.com,reciever2@reciever.com')
     - emailDetails.emailSubject: Prefix for the Subject line of the email (e.g. 'Subject Prefix |')
     - emailDetails.emailPreamble: Prefix for the Subject line of the email (e.g. 'Subject Prefix |')
     
     - smtpServer = SMTP server IP or hostname with the SMTP port number 'smtp.server.com:port'
     
     - emailUsername = email log in for the SMTP server (e.g. 'smtpuser@smtpserver.com')
     - emailPassword = password for the log in 
     
     - attachmentDirectory = 'Full Path to the directory on the local server where thee attachment files are located'
    
    
# Usage

Execute the python file from the 'email-with-attachments' directory

    $ python3 email-with-attachment.py
    
The python framework will pick the latest .csv file from the configured directory and send it to the configured recipients
    
# Output

The following output will be displayed i.e. the attachment file name and the list of recipients:

    "Your attachment [attachment1.csv] to the recipients [recipent1@recipient.com, recipent2@recipient.com] has been emailed"
