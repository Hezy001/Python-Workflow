sentence="This is a common interview question"

char_occurences={}
for char in sentence:
    if char in char_occurences:
        char_occurences[char]+=1
    else:
        char_occurences[char]=1
        
char_occurences_sorted=sorted(char_occurences.items(),key=lambda item:item[1],reverse=True)
print(char_occurences_sorted[0])
# lambda item: item[1]
# or
# def get_value(item):
#     return item[1]
#  item: item[1] means:
# "Take some variable called item, and return the second thing in it."

# Why item[1]?

# Because in a tuple like:

# python
# Copy
# Edit
# ('a', 3)
# item[0] is 'a'

# item[1] is 3

# So:

# python
# Copy
# Edit
# lambda item: item[1]
# Just means:

# "Look at the second part (the value/frequency) of each pair."

