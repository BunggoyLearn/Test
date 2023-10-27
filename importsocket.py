import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))

#This is what we use to hook up to the web
#'data.pr4e.org' is the host and 80 is the port we use