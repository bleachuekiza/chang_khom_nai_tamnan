import os
from time import sleep

data_prog = [
    {
        'nameprog':'VLC' , 
        'Status':'non-Prepare' , 
        'code': ' vlc'
    },
    {
        'nameprog':'Google Chrome' , 
        'Status':'non-Prepare' , 
        'code': ' googlechrome'
    },
    {
        'nameprog':'Winrar' , 
        'Status':'non-Prepare' , 
        'code': ' winrar'
    },
    {
        'nameprog':'Line' , 
        'Status':'non-Prepare' , 
        'code': ' line'
    },
    {
        'nameprog':'VSCode' , 
        'Status':'non-Prepare' , 
        'code': ' vscode'
    },
    {
        'nameprog':'Git' , 
        'Status':'non-Prepare' , 
        'code': ' git'
    }
]

def install_pros():
    cmdcode = 'choco install'
    for i in range(len(data_prog)):
        if data_prog[i]['Status'] != 'non-Prepare':
            cmdcode = cmdcode + data_prog[i]['code']

    print(cmdcode+' -y')
    exit()

if __name__ == "__main__
    while True:
        os.system('cls')
        print('[ List Program ]')
        for i in range(len(data_prog)):
            print('[{}] {:15}[{:^13}]'.format(i+1, data_prog[i]['nameprog'], data_prog[i]['Status']))
        print('[i] {:15}'.format('install program'))
        print('[x] {:15}'.format('exit program'))
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
