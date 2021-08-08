import ctypes, os
import subprocess
from time import sleep
from data import *

run1 = True
coder = 'Program by Zachtix (Atthwut Smith)'

def mainmenu():
    while True:
        os.system('cls')
        print('[ List Program ]')
        for i in range(len(data_prog)):
            print('[{:2}] {:20}[{:^13}]'.format(i+1, data_prog[i]['nameprog'], data_prog[i]['Status']))
        print('[i] {:15}'.format('install program'))
        print('[x] {:15}'.format('exit program'))
        print(coder)
        choibeinput = input('Choose Program : ')
        
        if choibeinput == 'i':
            install_pros()
        elif choibeinput == 'x':
            break
        else:
            try:
                if data_prog[int(choibeinput)-1]['Status'] == 'non-Prepare':
                    data_prog[int(choibeinput)-1]['Status'] = 'Prepare'
                elif data_prog[int(choibeinput)-1]['Status'] == 'Prepare':
                    data_prog[int(choibeinput)-1]['Status'] = 'non-Prepare'
            except:
                print('!!!Error')
                sleep(1)

def install_pros():
    cmdcode = 'choco install'
    while True:
        for i in range(len(data_prog)):
            if data_prog[i]['Status'] != 'non-Prepare':
                cmdcode = cmdcode + data_prog[i]['code']
        # print(cmdcode+' -y')
        os.system(cmdcode+' -y')
        print("install sucess")
        print(coder)
        sleep(3)
        exit()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def install_choco():
    x = 'powershell.exe Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))'
    os.system(x)
    os.system('cls')
    print(coder)
    sleep(1)
    print('\ninstall chocolatey sucess')
    print('\n\nPls open program again')
    sleep(1)
    print('Close program . . .')
    print('\n3 . . .')
    sleep(1)
    print('\n2 . .')
    sleep(1)
    print('\n1 .')
    sleep(2)
    exit()

if __name__ == "__main__":
    print(coder)
    if is_admin():
        print("Run as Admin success")
        try:
            subprocess.check_output('choco -?')
            print("Chocolate is installed")
            sleep(1)
            mainmenu()
            
        except:
            print("Chocolate is not installed")
            sleep(1)
            install_choco()
    else:
        print("Pls open program as Admin")
        sleep(5)