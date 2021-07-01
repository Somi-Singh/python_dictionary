dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':200}
max1=0
max2=0
max3=0
empty=[]
for i in dict:
    for k in dict:
        if dict[k]>max1:
            max1=dict[k]
        elif max1>dict[k] and max2<dict[k]:
            max2=dict[k]
        elif max2>dict[k] and max3<dict[k]:
            max3=dict[k]
empty.append(max1)
empty.append(max2)
empty.append(max3)
print(empty)