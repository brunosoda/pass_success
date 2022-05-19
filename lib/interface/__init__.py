from pass_success.lib.archive import *
import csv


def readInt(msg):
    while True:
        try:
            ni = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Enter an integer number.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUser preferred to stop the program.\033[m')
            return 0
        else:
            return ni


def line(size=50):
    print('-' * size)


def header(msg):
    print()
    line()
    print(msg.center(50))
    line()


def menu(options):
    c = 1
    for sample in options:
        print(f'\033[33m{c} - {sample}\033[m')
        c += 1
    s1 = readInt('\nChoose the first sample: ')
    return s1


def listing(file):
    """
    To transform simple data into list only. If you want to transform a data into a table, use def table
    :param file: name of the file and its type
    :return: a list
    """
    try:
        a = open(file, 'rt')
    except:
        print('An error occurred to open the file')
    else:
        psp_in_list = []
        for match in a:
            match = match.replace('\n', '')
            psp = float(match)
            psp_in_list.append(psp)
        return psp_in_list


def sem(sd1, sd2, n1, n2):
    return f'{(((sd1 ** 2) / n1) + ((sd2 ** 2) / n2)) ** (1/2):.2f}'


def tstat(avg1, avg2, se):
    if avg1 - avg2 < 0:
        return (avg2 - avg1) / se
    else:
        return (avg1 - avg2) / se


def dfis(n1, n2):
    """
    it calculate the degrees of freedom of two independent samples
    :param n1: size of the sample 1
    :param n2: size of the sample 2
    :return: degrees of freedom
    """
    return n1 + n2 - 2


def table(arc):
    with open(arc, 'r') as archive:
        archive_csv = csv.reader(archive, delimiter=';')
        new_list = []
        for i, line in enumerate(archive_csv):
            new_list.append(line)
    return new_list

