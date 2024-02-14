str1 = 'abcabccdbabcdefwwerew'

istart = 0
iend = 0
count = 0
substr = ''
substrfinal = ''
for i in range(0,len(str1)-1):
    for j in range(i,len(str1)):
        if str1[j] not in substr:
            substr+=str1[j] 
        else:
            if len(substr)> len(substrfinal):
                substrfinal = substr
                substr=''
            
            

print(substrfinal, count)