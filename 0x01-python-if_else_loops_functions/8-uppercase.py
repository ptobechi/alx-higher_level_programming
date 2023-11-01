 #!/usr/bin/python3

 def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - 32)
        else:
            upper = char
        print(upper, end='')
