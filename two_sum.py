
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
        
