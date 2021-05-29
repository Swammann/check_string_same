#
#
#
import sys


def readString():
    string = []
    in_string = None
    print()
    fname = input('enter the name of the file you wish to open: ')
    with open(fname, 'r') as f:
        in_string = f.read()
        nstring = input('how many strings do you want to read: ')
        splitline = in_string.split(',')
        for i in range(int(nstring)):
            string.append(splitline[i])
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
    for i in range(len(string_1)):
        if string_1[i] == string_2[i]:
            same = 'These files contain matching strings'
        else:
            same = "These files don't contain any matching strings"
    print()
    return print(same)


def main():
    try:
        string1 = readString()
        string2 = readString()
        string1 = spaceStrip(string1)
        string2 = spaceStrip(string2)
        checkString(string1, string2)
    except (OSError, UnboundLocalError) as err:
        print('\n -- Error with file open -- \n')
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    main()

