import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(2)

host = input("[*] Enter the Host To scan:  ")


def portscanner(port):
    if sock.connect_ex((host, port)):
        print ("[!!] Port %d is closed" % (port))
    else:
        print ("[+] Port %d is opened" % (port))

for port in range(1, 100):
    portscanner(port)