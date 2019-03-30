#!_*_coding:utf-8_*_
import socket
client = socket.socket()

client.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)
    print("命令结果大小：",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)#每次收到的有可能小于1024，所以必须有len判断
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.dacode())

client.close()