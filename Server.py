import socket
from datetime import datetime as dt
import datetime

serverName = '127.0.0.1'
serverPort = 2205

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
serverSocket.listen()

# socket props
message_timeout = 120
serverSocket.settimeout(message_timeout)

print("The server is ready to receive:")

listenForMessage = True
timeout_Timer = dt.now()
try:
    conn, addr = serverSocket.accept()
    while listenForMessage:
        try:
            message = conn.recv(2048)
            modifiedMessage = message.decode().upper()
            conn.send(modifiedMessage.encode())
            if message:
                timeout_Timer = dt.now()
            elif (dt.now() - timeout_Timer) >= datetime.timedelta(seconds=message_timeout):
                listenForMessage = False
                print("It looks like you've waited too long to send a message. ")

        except BlockingIOError as e:
            pass

        except Exception as e:
            print(e)
except socket.timeout:
    listenForMessage = False
    print("It looks like you've waited too long to send a message. ")
