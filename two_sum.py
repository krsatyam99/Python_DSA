
l1 =[1,9,4,7,8,3,5,11,13,87]
print(len(l1))
target = 94
# two sum problem solution 
# Step 1
my_map ={}
for index,value in enumerate(l1):
    compliment = target-value
    
    # print(index,value,"iiiijkbkjhkbh")
   
    if my_map.get(compliment) is not None:
        a= my_map.get(compliment)
        # print(a,"lll",index)
        print(f'the combination are {[a,index]} for value {[compliment,l1[index]]} for {target}' )
    else:
        my_map.update({value:index})
        # print(my_map)

 ## my code
a = [12,8,5,6,9,0,4,0,8,3]
target = 13
n = len(a) 
flag = False
for i in range(n):
    for j in range(i+1,n):
        if a[j] == target-a[i]:
            print(f"{i,j} along with {a[i]} and {a[j]} for {target} ")
            flag = True
    if flag:
        break
else:
    print("not found")
        
