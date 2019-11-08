# In obedience to the truth

# UVa 10082

keb = r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"

mapkb = { char.upper():lchar.upper()
         for char, lchar in [(keb[i], keb[i-1])
                             for i in range(1, len(keb))]
         if char not in r'`qaz'
        }


while True:
    try:
        s = input()
    except EOFError:
        break
    ans = ''
    for c in s:
        ans = ans + (mapkb[c] if c is not ' ' else c)
    print(ans)



