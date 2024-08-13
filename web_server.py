from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6789))  # Replace 6789 with your desired port number
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

message = connectionSocket.recv(1024).decode()

try:
    filename = message.split()
    f = open(filename[1:])
    outputdata = f.read()
    
    # Send HTTP header
    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    
    # Send the content of the requested file[^9^][9]
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    
    connectionSocket.close()
except IOError:
    # Send 404 Not Found response
    connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    connectionSocket.close()

serverSocket.close()
