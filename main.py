import ctypes, os
import subprocess
from time import sleep

data_prog = [
    {'nameprog':'VLC' , 'Status':'None' , 'code': ' vlc'},
    {'nameprog':'Google Chrome' , 'Status':'None' , 'code': ' googlechrome'},
    {'nameprog':'Winrar' , 'Status':'None' , 'code': ' winrar'},
    {'nameprog':'Line' , 'Status':'None' , 'code': ' line'},
    {'nameprog':'VSCode' , 'Status':'None' , 'code': ' vscode'},
    {'nameprog':'Git' , 'Status':'None' , 'code': ' git'}
    ]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def installpro():
    chococmd = 'choco install'
    xpro = ' vlc'
    print(chococmd + xpro + ' -y')
    # os.system(chococmd + xpro + ' -y')

if is_admin():
    print("Admin success")
    try:
        subprocess.check_output('choco -?')
        print("Chocolate is installed")
        installpro()
    except:
        print("Chocolate is not installed")
else:
    print("Pls open program as admin")
    sleep(5)