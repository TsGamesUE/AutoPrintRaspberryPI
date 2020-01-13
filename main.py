#!/usr/bin/env python#
# Send eMail to printer  

import sys
import imaplib

IMAP_SERVER = 'imap.gmail.com'
EMAIL_ACCOUNT = "notatallawhistleblowerIswear@gmail.com"
EMAIL_PASSWORD = 'secread Passwords'

def connect(IMAP_SERVER, EMAIL_ACCOUNT, EMAIL_PASSWORD):
    imap = imaplib.IMAP4_SSL(IMAP_SERVER)
    imap.login(EMAIL_ACCOUNT,EMAIL_PASSWORD)
    return imap

def disconnect(imap):
    imap.logout()

def main():
   imap = connect(IMAP_SERVER, EMAIL_ACCOUNT, EMAIL_PASSWORD) 


if __name__ == "__main__":
    main()