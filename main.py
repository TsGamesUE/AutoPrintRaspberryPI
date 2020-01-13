#!/usr/bin/env python#
# Send eMail to printer  

import sys
import imaplib
import os
import tempfile
import subprocess
import glob

from imap_tools import MailBox, Q

import json
isascii = lambda s: len(s) == len(s.encode())

with open('config.json') as config_file:
   conf = json.load(config_file)


IMAP_SERVER = conf['IMAP_SERVER']
EMAIL_ACCOUNT = conf['EMAIL_ACCOUNT']
EMAIL_PASSWORD = conf['EMAIL_PASSWORD']
PRINTER_NAME = conf['PRINTER_NAME']

def ASCII(s):
    x = 0
    for i in range(len(s)):
        x += ord(s[i])*2**(8 * (len(s) - i - 1))
    return x


def create_tmp_files(mailBody):
    msg = ASCII(mailBody)
    print(msg)
    msg = mailBody
    #mailBody.encode(encoding='ASCII')
    print(msg)
    tmp = tempfile.NamedTemporaryFile()
    try:
        tmp.write(msg.encode('ascii','ignore'))
        tmp.seek(0)
        print (tmp.name)
        subprocess.run(["lp", "-d", PRINTER_NAME, os.path.abspath(tmp.name)])
    finally:
        tmp.close()



         

def main():

    with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    #    for msg in mailbox.fetch(Q('UNSEEN')):
        for msg in mailbox.fetch():

            mailBody = msg.text
            print(isascii(mailBody))
            create_tmp_files(mailBody)



    
    

if __name__ == "__main__":
    main()