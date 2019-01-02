def obter_mais_longa_substring(s):
    maior = ''
    atual = []
    for c in s:
        atual += c
        if atual != sorted(atual):
            atual = [c]
        elif len(atual) > len(maior):
            maior = ''.join(atual)

    return maior

s = 'azcbibibegghakl'
print(obter_mais_longa_substring(s))
