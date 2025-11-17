

abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar_encrypt(abc, offset, txt):
    txt = txt.lower()
    result = ''
    txt = txt.replace(' ','')
    for i in range(len(txt)):
        for j in range(len(abc)):
            if txt[i] == abc[j]:
                result += abc[(j + offset) % 25]
    return result


def caesar_decrypt(abc, offset, txt):
    result = ''
    for i in range(len(txt)):
        for j in range(len(abc)):
            if txt[i] == abc[j]:
                result += abc[(j - offset) % 25]
    return result



def fence_encrypt(txt):
    txt = txt.replace(' ', '')
    res = ''
    res1 = ''
    for i in range(len(txt)):
        if i % 2 == 0:
            res += txt[i]
        else:
            res1 += txt[i]
    return res + res1


def fence_decrypt(txt):
    result = ''
    x = len(txt)
    y = x // 2
    for i in range(len(txt)//2):
        result += txt[i]
        result += txt[y + i + (x % 2)]
    if x % 2 == 1:
        result += txt[x // 2]
    return result
