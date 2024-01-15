import array as arr

n = int(input())

a=list(map(int, input().strip().split(" ")))

b = []

i = 0

for i in range(n-1):
    if(a[i] < a[i+1]):
        continue

    else:
        a[i] = (a[i]+a[i-1])/2

for i in range(n-1):
    if(a[i] < a[i+1]):
        b.append("Yes")
    else:
        b.append("No")

c = 0

for i in b:
    if(i == "No"):
        c = c + 1

if(c > 0):
    print("No")
else:
    print("Yes")

    
