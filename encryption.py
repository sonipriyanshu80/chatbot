n=input("enter a string")
key=int(input("enter a key"))
def encryp():
    enc=""
    for ch in n:
        if ch.isupper():
            lc = chr((ord(ch)-65 +key)%26+65)
            enc+=lc
        elif ch.islower():
            lc = chr((ord(ch)-97 +key)%26+97)
            enc+=lc
        else:
            enc+=lc
    print("result",enc)
def decryp():
    dec=""
    enc=""
    '''for ch in n:
        if ch.isupper():
            lc = chr((ord(ch)-65 +key)%26+65)
            enc+=lc
        elif ch.islower():
            lc = chr((ord(ch)-97 +key)%26+97)
            enc+=lc
        else:
            enc+=lc'''
    for ch in n:
        lc = chr(ord(ch)+key)
        enc+=lc
    for ch in enc:
        lc = chr(ord(ch)-key)
        dec+=lc
    print("result",dec)
encryp()
decryp()





output
enter a stringaBCde
enter a key27
result bCDef
result aBCde
