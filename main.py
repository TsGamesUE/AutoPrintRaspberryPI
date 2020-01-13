#!/usr/bin/env python#
# Send eMail to printer  

import sys
import imaplib
import os
import tempfile
import subprocess
import glob

from imap_tools import MailBox, Q
IMAP_SERVER = ''
EMAIL_ACCOUNT = ""
EMAIL_PASSWORD = ''
PRINTER_NAME = ''

def create_tmp_files(mailBody):
    tmp = tempfile.NamedTemporaryFile()
    path  = tempfile.gettempdir()    
    try:
        tmp.write(b'mailBody')
        tmp.seek(0)


        subprocess.run(["lp", "-d", PRINTER_NAME, tmp.name])
    finally:
        print('the_end')
        tmp.close()



         

def main():
    with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
        for msg in mailbox.fetch(Q('UNSEEN')):
            print (msg.text)
            mailBody = msg.text
            create_tmp_files(mailBody)


   # create_tmp_files('test')
    

if __name__ == "__main__":
    main()