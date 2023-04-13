fhand = open('2.txt')
#Open() opens a file that you name
count = 0
for line in fhand:
    count = count + 1
#Run a for loop that runs through the entire txt file and counts 1 for every new line (/n)
print('Line Count: ', count)


hhand = open('2.txt')
inp = hhand.read()
print(len(inp))
#opens a txt file, reads through it, puts it all on a single line and prints the amount of characters the line uses using len()
print(inp[:4])
#Prints from that line however much you ask it to

ghand = open('2.txt')
for line in ghand:
    line = line.rstrip()
    #This program automatically gives the strings a /n (new line) so
    #we use .rstrip() to erase the right white space which includes /n
    if line.startswith('2'):
        print(line)
        #We find all lines that start with '2' and then print them

        khand = open('2.txt')
        #This is another way of doing the above
for line in khand:
    line = line.rstrip()
    if not line.startswith('2'):
        continue
    #continue acts like a skip here, saying if it doesn't start with 2
    #start on the next line and try again
    print(line)
        #We find all lines that start with '2' and then print them

jhand = open('2.txt')
for line in jhand:
    line = line.rstrip()
    if not '2' in line:
        continue
    print(line)
#Another way to do this using the in command