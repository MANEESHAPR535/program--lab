# Python program to print positive Numbers in a List 
  
list1 = [5, -6, 0, 3, -7, 8] 
for num in list1:  
    if num >= 0:
    
       print(num)
       
       
 #square of numbers
       
for n in [0,1,2,3,4]:
    square = n**2
    print( n,'squared is',square )
    
#from a list of vowels select a from a given word
    words = ['apple', 'orange', 'pear', 'milk', 'otter', 'snake','iguana','tiger','eagle','usha']
vowel=[]
for word in words:
    if word[0] in "ae":
        vowel.append(word)
print ("===========vowels======\n",vowel)

