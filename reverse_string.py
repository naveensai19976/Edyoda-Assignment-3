def rev(str1):

    str = ''
    index = len(str1)
    while index > 0:
        str += str1[ index - 1 ]
        index = index - 1
    return str
print(rev('1234abcd'))