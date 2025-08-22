l1 = [2,4,6,8,12,16,18,14,20,]
sublist = l1[2:5] #slicing
print(sublist)

l2 = [num*100 for num in l1 if num % 2 == 0] #if stmt wont works when assigned a string in list
print(l2, end='\n')  

l3 = [num for num in range(1, 20) if num % 1 == 0] #**2 for square,*100  
#[expression for item in iterable if condition]
print(l3)
l4 = ['Sai','kAka','raMa','kimA','koMa']
l5 = [name.title() for name in l4]
l5 = [name.capitalize() for name in l4]
l5 = [name.casefold() for name in l4]
l5 = [name.capitalize() for name in l4]
print(l5)# mutable datatype

t1 = (2,3,4,5,6)
t1.count(3)
print(t1.count(3))

s1 = set()
s1.add(2)
s1.add(3)#no duplicates
print(s1) #dict

d1 = {'a':"sas",'b':2,'c':3}
print(d1['a'])
if d1.get('t') is None:
    print("key is not present")
print(d1.get('t'))
# no key then NONE
tree = ''
#alsway the value of empoty string is false
if  not tree:
    print("tree is not empty")
else:
    print("tree is empty")