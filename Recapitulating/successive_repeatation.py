def successive_repetition(s):
   
    res=s[0]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            res+='*'
        else:
            res+=s[i]
    return res
s=input("enter any string :")
print(successive_repetition(s))