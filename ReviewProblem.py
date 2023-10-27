name = input('Enter file:')
handle = open(name)
#We input the name of the file and then open it under the variable handle

counts = dict()
#we create a dictionary under the name counts
for line in handle:
#We look for the variable line inside of the text file which is under the variable handle
    words = line.split()
#We create the words variable by splitting the string 
    for word in words:
#We create word to count as the variable for the output of the next loop
        counts[word] = counts.get(word,0) + 1
#We fill the dictionary counts with a histogram that creates a new section for every new word(same name as the variable)
#and mark the value of that word starting initially at 0, but since it is counted 1 will be added to it

bigcount = None
bigword = None
#We create bigcount and bigword variables and list them as None
#None is different than 0, is more absolute and can be overwritten so math doesn't force a traceback

#the variables we have to play with now will be word, count, counts, bigcount, and bigword
#EXAMPLE USING items.txt
#word: The items listed in the dictionary and their associated value (how much words there are)
#count:The variable we will create for bigcount to display the value (" ") 
#counts: This is out dictionary which we will pull keys and values out of
#bigcount: starts at None and is changed to whatever count reflects and then is printed at the end
#bigword: starts at None and is changed to whatever word reflects and then is printed at the end
for word,count in counts.items():
#Loop will pull two variables(word,count) out of the dictionary(counts) using .items()
    if bigcount is None or count > bigcount:
#if statement is created and given a function that will run and run until it finds the largest number and becomes that number
#"If i am smaller than the next thing introduced, I am now the new thing, and so on and so forth"
        bigword = word
#bigword is easier because you just take the value from bigcount, see the key attached to it and then paste it
        bigcount = count

print(bigword,bigcount)
#Finally print the two variables and it should be BR, 32
    
