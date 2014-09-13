def anybase(num,base):
    convString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num//base == 0:
        return convString[num%base]
    else:
        return anybase(num//base,base)+convString[num%base]

print anybase(8,2)
