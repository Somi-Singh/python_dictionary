my_list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
list=[]
for dic in my_list:
    for key in dic:
        if (dic[key]) not in list:
            list.append(dic[key])
print(list)