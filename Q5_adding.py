list1=['one','two','three','four','five']

list2=[1,2,3,4,5,] 
i=0
empty={}
while i<len(list1):
    empty[list1[i]]=list2[i]
    i=i+1
print(empty)

