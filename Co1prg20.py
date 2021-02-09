#From a list of integers, create a list removing even numbers.

list = [2, 3, 16, 7, 22]
print( "Original list:",list)

for i  in list:
  if(i%2 == 0):
     list.remove(i)
print("list after removing Even numbers:",list)
