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
            stripped = spaceStrip(string)
    except OSError as err:
        print(' -- Error with file open -- ')
        print(err)
        print()
    f.close()
    return stripped


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
    return same


def main():
    string1 = readString()
    string2 = readString()
    print(checkString(string1, string2))


if __name__ == '__main__':
    main()


