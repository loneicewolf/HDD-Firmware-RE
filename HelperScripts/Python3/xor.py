def xor(data,key):
    b= ""
    keylen = len(key)
    for i in range(0,len(data)):
      b += chr(ord(data[i]) ^ ord(key[i % keylen]))
      print()
    return b



# usage:
# xor
# s="hello"
# key="password"
# xor(s,key)
# '\x18\x04\x1f\x1f\x18'


## or, using a loop:

# for c in s:
#    #print(chr(ord(c) ^ ord(key[i % keylen])))
