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


def remove_umlaut(string):
    """
    Removes umlauts from strings and replaces them with the letter+e convention
    :param string: string to remove umlauts from
    :return: unumlauted string
    """
    u = 'ü'.encode()
    U = 'Ü'.encode()
    a = 'ä'.encode()
    A = 'Ä'.encode()
    o = 'ö'.encode()
    O = 'Ö'.encode()
    ss = 'ß'.encode()

    string = string.encode()
    string = string.replace(u, b'ue')
    string = string.replace(U, b'Ue')
    string = string.replace(a, b'ae')
    string = string.replace(A, b'Ae')
    string = string.replace(o, b'oe')
    string = string.replace(O, b'Oe')
    string = string.replace(ss, b'ss')

    string = string.decode('utf-8')
    return string
         

def main():

    with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
        for msg in mailbox.fetch(Q('UNSEEN')):
        for msg in mailbox.fetch():

        mailBody = msg.text
        create_tmp_files(remove_umlaut(mailBody))



    
    

if __name__ == "__main__":
    main()
