total = 0
count = 0
while True :
    inp = input('Enter Number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)

#This is a loop that takes the average of a bunch of
#numbers, and then spits out the total, but can be done
#better using a list

numlist = list()
#create a list
while True :
    inp2 = input('Enter a number: ')
    if inp2 == 'DONE' : break
    valuu = float(inp2)
    #input same code as before
    numlist.append(valuu)
    #rather than add to count, just append the list

avg = sum(numlist) / len(numlist)
#do regular commands to the list to make an avg sum/len
print('Your average is:' , avg)

#Instead of having to construct a count and total number,
#the list just does that for you, and you can just focus on
#getting the average by messing with the list rather than
#constructing a lot of attached strings