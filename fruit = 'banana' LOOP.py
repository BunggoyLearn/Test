fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (index,letter)
    index = index + 1
    #creates a loop that lists the letter and its position for the entire string

vegetable = 'artichoke'
vletter = vegetable[index]
for vletter in vegetable:
    print(vletter)
#This is a faster to type loop if you only want it spelled

word = 'zucchini'
count = 0
for cletter in word:
    if cletter == 'c':
        count = count + 1
print(count)
#everytime we see a 'c' we add 1 to the counter to give us 2