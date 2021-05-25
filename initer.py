import pathlib
import os
import json

def Whoami():
    return (str(pathlib.Path.home()))

def UserConf(username, email):
    conf_path = str(Whoami()) + '/.local/share/to.conf'
    with open(conf_path, 'w') as fli:
        conf_fli = {'username':username,'email':email}
        conf_fli = json.dumps(conf_fli, indent=4)
        fli.write(conf_fli)