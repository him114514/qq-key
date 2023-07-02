import socket
import sys
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'cn-yw-plc-1.openfrp.top'

port = 44241

s.connect((host, port))

msg = s.recv(3000)
print(msg.decode('utf-8'))
time.sleep(20)
