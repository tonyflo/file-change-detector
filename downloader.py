import os
import shutil
import urllib.request
from datetime import datetime
from hasher import sha1
from notifier import send_notification

def move_files(filename):
    shutil.copy(filename, '/root/campbell/updates/')
    os.rename(filename, '/root/campbell/latest.pdf')

def check_for_update():
    # get date and time as string
    now = datetime.now()
    filename = '/root/campbell/{}.pdf'.format(now.strftime("%Y%d%m%H%M%S"))
    
    # download file
    url = 'https://tonyteaches.tech/test.pdf'
    urllib.request.urlretrieve(url, filename)
    
    # get hashes
    try:
        hash_latest = sha1('/root/campbell/latest.pdf')
    except:
        move_files(filename)
        print('First file saved')
        return
    hash_new = sha1(filename)
    
    # compare hashes
    if hash_latest != hash_new:
        print('Found update')
        move_files(filename)
        send_notification(url)
    else:
        print('No update')
        os.remove(filename)

check_for_update()
