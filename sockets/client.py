from comm import sendAndReceive

ip = "127.0.0.1"
port = 59899
data = "".join(["a"]*(4096*1000+55))

sendAndReceive(ip,port,data)
