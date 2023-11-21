# Write a function that takes a string of lower case english alphabet letters and return index the string first non repeating character, Means it occurs only ones,if there is no such data return -1.

def string_checker(s):
    counting_character = 0
    if (s.isupper()) == False :
        print("input is in lower case")
        for index,value in enumerate(s):
            a=s.count(value)
            # print(a)
            if a ==1 :
                print([index , s[index]])
                break
        else:
            print(-1)
string_checker(s = 'allkttioiokuyyukb' ) #input is in lower case [0, 'a']
