num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
res = dict()
for key in sorted(num):
    res[key] = sorted(num[key])
print("The sorted dictionary : " +str(res)) 

