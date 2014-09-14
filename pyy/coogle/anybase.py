def anybase(num,base):
    syms = "0123456789ABCDEFGH"
    if num//base == 0:
        return syms[num%base]
    else:
        return anybase(num//base,base)+syms[num%base]

print anybase(20,16)
