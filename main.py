#
#
#

def readString():
    string = []
    in_string = None

    print()
    fname = input('enter the name of the file you wish to open: ')
    try:
        with open(fname, 'r') as f:
            in_string = f.read()
            nstring = input('how many strings do you want to read: ')
            splitline = in_string.split(',')
            for i in range(int(nstring)):
                string.append(splitline[i])
    except OSError as err:
        print(' -- Error with file open -- ')
        print(err)
        print()
    f.close()
    return string


def spaceStrip(string_list):
    strip = []
    for line in string_list:
        string_list.strip()


def checkString():
    ...


if __name__ == '__main__':
    string = readString()

