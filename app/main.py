# Uncomment this to pass the first stage
import socket
import _thread

def processRequest(conn):
    while True:
        request = conn.recv(4096)
        # print(request)

        decodedRequest = request.decode("utf-8")
        requestParams = decodedRequest.split('\r\n')
        print(requestParams)

        requestParamsCount = int(requestParams[0][1:])
        # print("number of params = ", requestParamsCount)

        if(requestParams[2].lower() == "ping"):
           conn.send(b"+PONG\r\n")
        elif(requestParams[2].lower() == 'echo'):
            conn.send(bytes("+" + requestParams[4] + "\r\n", "utf-8"))

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen(10) # 10 is the backlog

    while True:
        conn, address = server_socket.accept() # wait for client
        _thread.start_new_thread(processRequest, (conn, ))
    
        # conn.shutdown(socket.SHUT_WR)
        # conn.close()


if __name__ == "__main__":
    main()
