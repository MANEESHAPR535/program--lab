
def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1 = {'aa': 1, 'ab': 8}
dict2 = {'ac': 3, 'ad': 9}
print(Merge(dict1, dict2))
print(dict2)