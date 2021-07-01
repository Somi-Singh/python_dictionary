students=[{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
sum=0
sum1=0
for i in students:
    sum=sum+i["id"]
    sum1=sum1+i["success"]
print(sum)
print(sum1)

