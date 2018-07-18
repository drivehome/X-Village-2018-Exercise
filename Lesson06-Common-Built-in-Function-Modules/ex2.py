def caesar_cipher(s, t):
    s=str(s)
    t=int(t)
    l=[]

    for i in range(len(s)):
        b = ord(s[i]) + t
        if b >= 120:
            b = b - 23
        l.append(chr(b))
    return ''.join(l)

print(caesar_cipher("xvillage", 3))