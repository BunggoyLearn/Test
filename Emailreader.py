#Good email reader to see how many emails you have
#Uses input so it is usable with everything
#if input fails it sends an error message and
#doesn't break
fname = input('Enter File Name here:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
    print('There were ', count, 'subject lines in ', fname )