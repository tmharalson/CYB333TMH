# client script which connects to server

import socket
host = '127.0.0.1'
port = 65432

def start_client(): # function to start client
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Connected to server at " + host + ":" + str(port))

            while True: # loop to send and receive messages
                message = input("Enter a message to send to server! Or type 'exit' to exit.\n")
                if message == 'exit': # if user types exit, break the loop
                    print("Exiting...")
                    break
                s.sendall(message.encode()) # send message to server if not exit
                data = s.recv(1024) # receive response from server (max 1024 bytes)
                print("Received response:", data.decode()) # decode response

    except ConnectionRefusedError: # handle connection refused error
        print("Connection refused.")
    except Exception as e: # handle any other exceptions
        print("An error occurred:", str(e))

if __name__ == "__main__":
    start_client()