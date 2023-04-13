fruit = 'banana'
#[b][a][n][a][n][a]
# 0  1  2  3  4  5
letter = fruit[1]
#[1] means look at the letter in position 1. REMEMBER: Starts at 0
print (letter)
#finds the position of the letter in banana and reports the letter back. 

x = 3
w = fruit[x-1]
#we can do math with the positions e.g. [x - 1]
print (w)
#3 - 1 is 2 so it takes position 2 'n' and says it

# zot = 'abc'
# print (zot[5])
#This does not work because the called letter extends further than the length of the string

print (len(fruit))
#len counts the amount of letters/digits in a string
#this one should be 6