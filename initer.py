import pathlib
import os
import json

'''
This file is responsible for creating a storage space
on the user's path (Linux, Mac, Windows)
to store to information and configurations
such as username and email.
'''

# In this function, the path of the home file is specified
def Whoami():
    return (str(pathlib.Path.home()))

'''
This function is to receive the
user's email and username and create the file in the specified path
of the previous function ((Whoami))
and then save the email and username in this
file in the form of Json
'''
def UserConf(username, email):
    # Get the type of operating system and choose to create a directory
    conf_path = None
    if os.name == "nt":
        conf_path = str(Whoami()) + '\\to.conf'
    else:
        conf_path = str(Whoami()) + '.local/share/to.conf'
    with open(conf_path, 'w') as fli:
        conf_fli = {'username':username,'email':email}
        conf_fli = json.dumps(conf_fli, indent=4)
        fli.write(conf_fli)

# Checking the file in the path
def IsInited():
    conf_path = None
    if os.name == "nt":
        conf_path = str(Whoami()) + '\\to.conf'
    else:
        conf_path = str(Whoami()) + '.local/share/to.conf'
    return os.path.exists(conf_path)
