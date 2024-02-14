def is_armstrong(num):
    sum1=0
    num = num
    while num>0:
        sum1+= (num%10)**3
        num = num//10
        
    print(sum1)
    return sum1
    
print(is_armstrong(154))

str1 ='asdfgh'
s = str1[:-1:]
print(s)
#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
'''
echo "# iques" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ankitsingh9code/iques.git
git push -u origin main


git remote add origin https://github.com/ankitsingh9code/iques.git
git branch -M main
git push -u origin main
'''