dict1={"a":1, "k":[98,97] ,"op":4}
list1 =[]
l2 =[]
for key,value in dict1.items():
    print(value)
    a =list1.append(value)
    b = l2.append(key)
    # print(a,b)
    
print(l2 , list1)
#1
#[98, 97]
#4
#['a', 'k', 'op'] [1, [98, 97], 4]
