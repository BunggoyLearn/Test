friends = ['Sally', 'Joseph', 'Glenn']
#This is a list, which we can assign to one variable
print(friends[1])

#fruit = 'Banana'
#fruit[0] = 'b'
#This does not work because strings are 'IMMUTABLE' which means they cannot be changed

lotto = [2, 14, 26, 35, 48]
print(lotto)
lotto[2] = 28
print(lotto)
#However, we can change lists because they are 'MUTABLE', so we just changed the 2nd positions number 

print(len(lotto))
# 'len' will count items in a list as they are seperated by the commas not all the spaces within it

print(list(range(4)))
#Range shows us a list (when we put it in one) 'list(range())' of the 'range' that is in the list
print(len(friends))
#We know the length of the list is 3
print(list(range(len(friends))))
#We get back a list counting the positions starting from 0

for friend in friends :
    print('Happy New Year,', friend,'!')

#for i in friends:
#    friend2 = friends[i]
#    print('Happy New Year,', friend2,'!')
# Ask Tio Paul about this

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
#Lists can be added together
d = b + a
print(d)
#It is not communitive (duh)

print(lotto[1:3])
#Lists can be sliced like strings

stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append(69.0)
print(stuff)
#.append adds things to the list, so we can use it to grow our list by adding whatever to the end of the list

some = [1,2,3,4,5,6,12]
print(5 in some)
print(9 in some)
print(10 not in some)
#True or false statements using in to verify whether items are in the list or not 

friends.sort()
#.sort can be used to sort items in a list alphabetically
print(friends)
print(friends[1])
#Changes the order of what friend is now in the 1st position