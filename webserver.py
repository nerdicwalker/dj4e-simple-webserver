from socket import *

def createServer():
    "Create a localhost server on port 9000."
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.bind(('localhost', 9000))
        serverSocket.listen(5)
        while(1):
            (clientSocket, address) = serverSocket.accept()

            rd = clientSocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0):
                print(pieces[0])
            
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello world!</body></html>\r\n\r\n"
            clientSocket.sendall(data.encode())
            clientSocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShuting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    
    serverSocket.close()

print("Browse to http://localhost:9000 to access the webserver.")
createServer()

