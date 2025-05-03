# port scanner

import socket
import sys
from datetime import datetime

def validate_port(port): # function to validate port number
    try: # convert port to integer
        port  = int(port)
        if 0 <= port <= 65535: # check if port is in valid range
            return port # return port if valid
        else: # if port is not in valid range, print error message
            print("Port number must be between 0 and 65535.")
            return None
    except ValueError: # handle value error if port is not an integer
        print("Invalid port number. Please enter a valid integer.")
        return None

# function to scan single port
def portscan(host, port): #function to scan a single port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # set timeout for socket connection

        result = sock.connect_ex((host, port))
        if result == 0:
            current_time = datetime.now().strftime("%H:%M:%S") # get current time
            print(f"[{current_time}] Port {port} is open.") # print if port is open
        else:
            current_time = datetime.now().strftime("%H:%M:%S") # get current time
            print(f"[{current_time}] Port {port} is closed.") # print if port is closed
            sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved.") # handle hostname error
        sys.exit() # exit program
    except socket.error:
        print("Could not connect to server.") # handle connection error
        sys.exit() # exit program

# function to control scanning process
def mainfunction():
    print("Port Scanner for Python\n")

    target = input("Enter target (must be localhost or scanme.nmap.org): ").strip()
    if target not in ['localhost', 'scanme.nmap.org']:
        print("Invalid target. Please enter 'localhost' or 'scanme.nmap.org'.")
        return

# get start port
    start_port = validate_port(input("Enter start port: "))
    if start_port is None:
        return

# get end port
    end_port = validate_port(input("Enter end port: "))
    if end_port is None:
        return

    if start_port > end_port: # check if start port is greater than end port
        print("Start port must be less than or equal to end port.")
        return

    print("\nScanning ports from " + str(start_port) + " to " + str(end_port) + " on " + target + "...\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Scan started at: {timestamp}\n")
    for port in range(start_port, end_port + 1):
        portscan(target, port)

    print("\nScanning completed.")

# run main function
if __name__ == "__main__":
    mainfunction()