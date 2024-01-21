def romantoint(s:str)->int:
    dict={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    s=s.replace('IV','IIII')
    s=s.replace('IX','VIIII')
    s= s.replace('XC', 'LXXXX')
    s= s.replace('XL', 'XXXX')
    s= s.replace('CD', 'CCCC')
    s= s.replace('CM', 'DCCCC')
    result=0
    for i in range(len(s)):
        result+=dict[s[i]] #DICT(S(0))=DICT(I)=1
    print(result)
romantoint('XII')
romantoint('C')
romantoint('LII')