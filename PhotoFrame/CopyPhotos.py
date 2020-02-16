import os
import pysftp
import random
from PhotoBaseFolder import PhotoBaseFolder

# Folder to load
Folder = r"D:\Photos_Freya"
Folder = "Y:\\"
photobasefolder = PhotoBaseFolder(Folder)

# Server settings
host='sftp.steurs.ch'
username='steurs.ch'
pkey='C:\\Users\\karel\\PycharmProjects\\RaspberryPi\\id_rsa_pw_open.pem'
pkey_pass='pwd'

# Load options
cnopts = pysftp.CnOpts()
hostkeys = None

if cnopts.hostkeys.lookup(host) == None:
    print("New host - will accept any host key")
    # Backup loaded .ssh/known_hosts file
    hostkeys = cnopts.hostkeys
    # And do not verify host key of the new host
    cnopts.hostkeys = None

with pysftp.Connection(host, username = username, private_key = pkey,private_key_pass=pkey_pass, cnopts = cnopts) as sftp:
    if hostkeys != None:
        print("Connected to new host, caching its hostkey")
        hostkeys.add(host, sftp.remote_server_key.get_name(), sftp.remote_server_key)
        hostkeys.save(pysftp.helpers.known_hosts())

    with sftp.cd('PhotoFrame'):
        for oldfile in sftp.listdir():
            sftp.remove(oldfile)
        for photo in photobasefolder.photolist:
            sftp.put(photo)
    sftp.close()
