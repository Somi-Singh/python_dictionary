string="w3resource"
count=0
a={}
for c in list(string):
    if c not in a:
        a[c]=0
    a[c]+=1
for key,value in a.items():
    print(key,value)