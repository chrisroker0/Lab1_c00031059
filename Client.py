import datetime
from socket import *
import os
from dotenv import load_dotenv
from inputimeout import inputimeout, TimeoutOccurred
from datetime import datetime as dt
from Message import Message

load_dotenv()

serverName = '127.0.0.1'
serverPort = 2205
clientSocket = socket(AF_INET, SOCK_STREAM)
message_timeout = 120
try:
    clientSocket.connect((serverName,serverPort))
    print("Welcome! To quit at any time use \"exit()\" to quit.")

    listenForMessage = True
    while listenForMessage:
        try:
            message = inputimeout(prompt='What message do you have for me? ', timeout=message_timeout)
            json_message = Message(message, dt.now()).convert_to_json()
            clientSocket.send(message.encode())

            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print(modifiedMessage.decode())
            if message == "exit()":
                clientSocket.close()
                listenForMessage = False
        except OSError as e:
            print("It looks like your server is not running on that port \n \
            Please ensure you have the correct Servername and port number \n \
            And your server is running.")
            clientSocket.close()
            listenForMessage = False
            if os.getenv("DEBUG"):
                print(e)
        except ConnectionRefusedError as e:
            print("It looks like your server is not running on that port \n \
            Please ensure you have the correct Servername and port number \n \
            And your server is running.")
            clientSocket.close()
            listenForMessage = False
            if os.getenv("DEBUG"):
                print(e)
        except TimeoutOccurred:
            print("It looks like you've waited too long to send a message. ")
            listenForMessage = False
        except Exception as e:
            print("e   ",e)

except ConnectionRefusedError as e:
    print("It looks like your server is not running on that port \n \
           Please ensure you have the correct Servername and port number \n \
           And your server is running.")
    clientSocket.close()
    listenForMessage = False
    if os.getenv("DEBUG"):
        print(e)
except Exception as e:
    print("e   ",e)
