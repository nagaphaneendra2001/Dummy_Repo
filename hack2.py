a =   (input())


str1=""
l = []

if(a[0] == "/"):
    l.append(a[0])
else:
    l.append("/")

for i in range(len(a)-1):
    if(a[i]==a[i+1] and a[i]=="/"):
        l.append("/")

    else:
        l.append(a[i])

for i in l:
    str1 += i 
print(str1)