text = "X-DSPAM-Confidence:    0.8475"
numstart = text.find(' ')
numwhite = text[numstart:]
numstr = numwhite.strip()
num = float(numstr)
print(num)
print(type(num))