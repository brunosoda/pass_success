from pass_success.lib.interface import *
from time import sleep


def readArchive(name):
    try:
        a = open(name, 'rt')
    except:
        print('An error occurred to open the archive')
    else:
        c = 1
        for match in a:
            data = match.split(';')
            data[0] = data[0].replace('\n', '')
            # sleep(0.1)
            print(f'Match {c}: {data[0]}% of pass success')
            c += 1
    finally:
        a.close()
