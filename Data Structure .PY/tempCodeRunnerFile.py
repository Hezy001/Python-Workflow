letters = ["a", "b", "c", "d"]
letters[0] = "A"  # Changes the first item in the list to a capital A
print(letters)
print(letters[:3])  # prints from the first to the third
print(letters[::2])  # This is a stepwise of 2


numbers = list(range(20))
print(numbers[::-1])  # Prints backwards starting from 19
##Lists unpacking
numbers=[1,2,3,5,6,7,8,89]
first, second, *other=numbers
print(first)
print(other)

##Looping over lists
letters=["a","b","c"]
for index, letter in enumerate(letters):  ####enumerate returns and iterable object i.e it returns a tuple
    print(index, letter)
    
##Adding or removing items from a list
letters=["a","b","c"]
letters.insert(0,"c") ##Adds something to a particular positon in a list
letters.append("d")  ##Adds a d to the end of the list
print(letters)

##Removing items from a list
letters=["a","b","c"]
letters.remove("a")
print(letters)

##Removing items from a list
letters=["a","b","c"]
letters.pop()    # Removes the last item from the list, you can also specify the index 
print(letters)

##You can also use the del function
letters=["a","b","c","d"]
del letters[0:3]
letters.clear()
print(letters)

## Finding items in a list
letters=["a","b","c"]
print(letters.count("d")) # Tells us how many times d occurs in the list 
if "d" in letters:
    print(letters.index("d")) # Returns the index of the item in the list
else:
    print("Not found")

## Sorting lists 
numbers=[ 3,51,2,6,8]
numbers.sort(reverse=True)  ##SOrts in a descending order
print(sorted(numbers)) # It returns a newly sorted list
print(numbers)

items=[
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
    
    
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

##or 

items=[
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
]

# Using lambda instead of the named function
items.sort(key=lambda item: item[1])
print(items)

##Map Functions

items=[
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
]
prices=[]
for item in items:
    prices.append(item[1])
print(prices)

#or Map function

items=[
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
]

x=map (lambda item:item[1], items)
for item in x:
    print(item)

##Filter Functions
items=[
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
]

x=filter(lambda item: item[1]>=10, items)
for item in x:
    print(item)

##List Comprehension ---Most efficient
items=[
    ("Product1",10),
    ("Product2",9),
    ("Product3",12)
]
filtered=[item for item in items if item[1] >=10]## Iterates over the items and returns the items that meet the condition i.e Greater than 10
print(filtered)

#Zip function 
list1=[1,2,3]
list2=[10,20,30]
print((list(zip("abc", list1,list2))))
###Stacks  ----LIFO (Last in first out)
browsing_session=[]
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last=browsing_session.pop()
print(last)
print(browsing_session)
print("redirect",browsing_session[-1])
if not browsing_session:
    print("disable")
    
##Queues --FIFO First in FIrst Out 
from collections import deque
import queue
queue=deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue) 
if not queue:     ## Incase when the queue is empty
    print("empty")    
    
##Tuples --- A read  only list   .....They are immutable
point=(1,2) + (3,4)  ## CONCATENATE A TUPLE 
print(point)

point=(1,2) *3   ####It repeats the tuple three times 
print(point)

point=tuple([1,2])  ###Converts a list to a tuple 

point=(1,2,3)
print(point[0:2])
x,y,z=point
if 10 in point:
    print("exists")
else:
    print("Doesn't exist")
    
##Arrays--Takes less memeory but performs faster
from array import array
numbers= array("i",[1,2,3])
numbers.append(4)
print(numbers)

##Sets-----Removes duplicates from a list
numbers=[1,1,2,3,4]
first=set(numbers)
second={1,5}

print(first | second )    ###it is called a union of two sets...

print(first&second) ### Intersctions
print(first-second) ###difference
print(first^second)##either in the first or the second but not both 

if 1 in first:
    print("yes")
    
##Dictionaries  ----- Collection of key valued pairs
# point={"x":1,"y":2}
# point=dict(x=1, y=2)
# point["x"]=10
# print(point)

point={"x":1, "y": 2}
point=dict(x=1,  y=2)
point["x"]=10
point["z"]=20
if "a" in point:
    print(point["a"])
print(point.get("a",0))
del point["x"]
print(point)

for key in point:
    print(key,point[key])
    
##Random work   _____ Dictionary comprehension
# values=[x * 2 for x in range(5)]
values={x:x * 2 for x in range(5)}
print(values)
    
####Generator expressions /objects - -Large dataset or infinite data
values=(x*2 for x in range(10) )
print(values)
for x in values:
    print(x)