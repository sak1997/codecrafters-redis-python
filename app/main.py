# Uncomment this to pass the first stage
import socket
import _thread

def sendPong(conn):
    while True:
        request = conn.recv(4096)
        conn.send(b"+PONG\r\n")
    # print("here")
    # conn.shutdown(socket.SHUT_WR)
    # conn.close()

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen(10) # 10 is the backlog

    while True:
        conn, address = server_socket.accept() # wait for client
        _thread.start_new_thread(sendPong, (conn, ))
        # request = conn.recv(4096)
        # conn.send(b"+PONG\r\n")
    
    conn.shutdown(socket.SHUT_WR)
    conn.close()


if __name__ == "__main__":
    main()
