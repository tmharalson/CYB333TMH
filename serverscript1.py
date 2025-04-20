# server script which listens for connections

import socket
host = '127.0.0.1' # the local host
port = 65432 # port to listen on

def start_server():
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((host, port)) # bind socket to host and port
      s.listen() # listen for incoming connections
      print("Server is listening on " + host + ":" + str(port))

      conn, addr = s.accept() # accept a connection
      with conn:
        print("Connected by", addr)  # print  address of client
        while True:
            data = conn.recv(1024) # receive data from client (max 1024 bytes)
            if not data:
                print("Connection closed by client") # if no data received, loop breaks
                break
            print("Received data:", data) # decode data
            conn.sendall(data) # send data to client
  except Exception as e: # handle any exceptions
    print("An error occurred:", str(e))

if __name__ == "__main__":
    start_server()