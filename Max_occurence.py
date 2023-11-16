# counting the occurence  of a specific number 


numbers = [1,4,6,9,11,15,15,15,15,17,21,34,34,56]
number_to_find = 15
counts =0
for i in numbers:
    if i == number_to_find:
        counts = counts+1
print(counts)




## Getting  the max occurence element 

numbers = [1, 4, 6, 9, 11,11,11,11,11,11, 15, 15, 15, 17, 21, 34, 34, 56]

max_occ_num = None 
max_occ_count = 0


data ={}
for i in numbers:
    if i in data:
        data[i]= data[i]+1
    else:
        data[i]=1
        
    if data[i]> max_occ_count:
        max_occ_count = data[i]
        max_occ_num = i
print(f"The max occuring number is {max_occ_num} having {max_occ_count} repeation ")
        
        

