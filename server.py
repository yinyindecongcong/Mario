import socketserver
import json
from socket import socket, AF_INET, SOCK_DGRAM
import time

client = {}
UDPsender = socket(AF_INET, SOCK_DGRAM)
UDPsender.bind(('localhost', 1234))
UDPlistener = socket(AF_INET, SOCK_DGRAM)
UDPlistener.bind(('localhost', 8022))

data1 = None
data2 = None
count = 1

def recv_from_all():
    for i in client.values():
        if not i[0]:
            return False
    return True

def send():
    for i in client.keys():
        client[i][0] = False
        if client[i][1] == 2:
            if data1:
                UDPsender.sendto(data1, i)
        elif client[i][1] == 1:
            if data2:
                UDPsender.sendto(data2, i)

if __name__ == '__main__':
    while True:
        data, addr = UDPlistener.recvfrom(1024)
        if addr not in client.keys():
            data = json.loads(data.decode())
            data['player1'] = (count == 1)
            data = json.dumps(data).encode()
            client[addr] = [True, count]
            count += 1
        if client[addr][1] == 1:
            client[addr][0] = True
            data1 = data
        else:
            client[addr][0] = True
            data2 = data
        if len(client) == 2 and recv_from_all():
            send()
