#!/usr/bin/env python#
# Send eMail to printer  

import sys
import imaplib
from imap_tools import MailBox, Q
IMAP_SERVER = '....kasserver.com'
EMAIL_ACCOUNT = ""
EMAIL_PASSWORD = ''

def connect(IMAP_SERVER, EMAIL_ACCOUNT, EMAIL_PASSWORD):
    imap = imaplib.IMAP4_SSL(IMAP_SERVER)
    imap.login(EMAIL_ACCOUNT,EMAIL_PASSWORD)
    return imap

def disconnect(imap):
    imap.logout()

def main():
    with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
        subjects = [msg.subject for msg in mailbox.fetch(Q('UNSEEN'))]
        print (subjects)
    

if __name__ == "__main__":
    main()