# binary search assignment 


numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15
left_index = 0
mid_index =0
right_index = len(numbers)-1

while left_index <= right_index: # binary search
    mid_index =(left_index+right_index)//2
    mid_number = numbers[mid_index]
    if mid_number == number_to_find:
        print(f"{mid_number} has been found on {mid_index}")
        
    if mid_number> left_index:
        left_index = mid_index+1
    else:
        right_index = mid_index-1
        
        
   
for index, value in enumerate(numbers): # linear search 
    mid_index =(left_index+right_index)//2
    mid_number = numbers[mid_index]
    if mid_number == number_to_find:
        print(mid_number)
