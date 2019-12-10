#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ''
    j = 0
    for i in (str):
        if (j == n):
            j += 1
        else:
            newstr += chr(ord(i))
            j += 1
    return newstr
