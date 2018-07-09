def swap_case(s):
    out = ''
    for i in s:

        if i.islower():
            i=i.upper()
        elif i.isupper:
            i=i.lower()
        out += i
    return out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)