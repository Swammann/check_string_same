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
    strip_list = []
    for line in string_list:
        strip = line.strip()
        strip_list.append(strip)
    return strip_list


def checkString(string_1, string_2):
    same = None
    for i in string_1:
        if string_1[i] == string_2[i]:
            same = 'These files contain matching strings'
        else:
            same = "These files don't contain any matching strings"
    return same


if __name__ == '__main__':
    string1 = readString()
    string2 = readString()
    stripped1 = spaceStrip(string1)
    stripped2 = spaceStrip(string2)
    print(checkString(stripped1, stripped2))

