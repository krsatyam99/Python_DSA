list_searching =[2,9,0,3,4,6,7,7,57,98]
to_find = 98
list_searching.sort()
print(list_searching)

### logic for linear search 
for index,value  in enumerate(list_searching): # in list if you want index as well as the value you can use enemurate
    if to_find == value:
        print( value, index ) # linear search 
        
        
        
### logic for binary search 
left_ind=0
right_ind=len(list_searching)-1
print(right_ind)
mid_ind=0



# print(mid_ind)
while left_ind <= right_ind:
    
    mid_ind=(left_ind + right_ind)//2  #we have used // instead of / because single / will return a decimal result 


    mid_number = list_searching[mid_ind]
    print(mid_number,"detail1")

    if mid_number == to_find :
        print(mid_ind,"found",mid_number)
        
    
    if mid_number < to_find:
        left_ind= mid_ind+1
        # print("right hand side shifted")
    else:
        right_ind= mid_ind-1
        # print("left hand side shifted")
else:
    print(f"{to_find} not found in the list")
        

        
    


    
    
    
