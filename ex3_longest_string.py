def obter_mais_longa_substring(s):
    aux = ''
    c = c2 = 0
    while c < len(s)-1:
        c2 = c + 1
        while s[c2] >= s[c]:
            if c2 < len(s)-1:
                c2 += 1
        c += 1
        if len(s[c:c2]) >= len(aux):
            aux = s[c:c2]
    return aux

s = 'azcbibibegghakl'
print(obter_mais_longa_substring(s))
