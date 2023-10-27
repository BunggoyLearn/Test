print(ord('H'))
print(ord('e'))
print(ord('\n'))
#This prints the value of H e and new line as what their ASCII(numerical) values are
# IN PYTHON 3 ALL STRINGS ARE UNICODE

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))

while True:
    data = mysock.recv(512)
    if (len(data) <1):
        break
    mystring = data.decode()
    #automatically decodes if it is UTF-8 or ASCII
    print(mystring)
  #turns bytes to Unicode

  