#Finad path to data file
import os

def pathtodata():
    current = str(os.getcwd()).split('/')
    path = ''

    for i in current:
        path += i
        path += '/'
        if i == 'Cryptorion':
            path += 'Data'
            break
    return path