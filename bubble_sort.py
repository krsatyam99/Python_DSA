# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")
elements=[1,8,3,4,19,5,0,1,0]
size1= len(elements)
# print(size)
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    
size = len(elements)
print(size,",dfkjd")

for i in range(0,size-1):
    for j in range(0,size-1-i):
        temp_dict= elements[j]['transaction_amount']
        if elements[j]['transaction_amount']>elements[j+1]['transaction_amount']:
            print("yes")
            elements[j]['transaction_amount']= elements[j+1]['transaction_amount']
            elements[j+1]['transaction_amount'] = temp_dict
            
            
            
print(elements)
            
            
            
            
