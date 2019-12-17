#!/usr/bin/python3
def no_c(my_string):
    newstr = ''
    for i in (my_string):
        if (chr(ord(i)) == 'c' or chr(ord(i)) == 'C'):
            continue
        else:
            newstr += chr(ord(i))
    return newstr
