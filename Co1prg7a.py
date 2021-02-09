
# Python code to find whether all  list have same length   
Input = [(5, 8, 10), (33, 45, 7)]  
print("Initial  two list ", Input) 
i= 3
flag = 1
for tuple in Input: 
    if len(tuple) != i: 
        flag = 0
        break
if flag: 
    print("the list are same length") 
else: 
    print("list does not have same length")
    print("sum")
    
    