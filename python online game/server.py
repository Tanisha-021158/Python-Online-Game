import socket
from _thread import *  # Import threading to handle multiple clients
import sys

# Define server IP and port
server = "192.168.1.8"  # Change this to the appropriate IP
port = 5560  # Port number for communication

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
try:
    s.bind((server, port))
    print("Socket successfully bound.")
except socket.error as e:
    print(f"Socket binding failed: {e}")
    sys.exit()  # Exit if binding fails

# Start listening for client connections (max 2 clients in the waiting queue)
s.listen(2)
print("Waiting for connections, server started.")

# Function to handle a client connection in a separate thread
def threaded_client(conn):
    conn.send(str.encode("Connected"))  # Send an initial message to the client
    while True:
        try:
            data = conn.recv(2048)  # Receive data (max 2048 bytes)
            if not data:  # If no data is received, the client has disconnected
                print("Disconnected")
                break
            reply = data.decode("utf-8")  # Decode received data
            print("Received:", reply)  # Print received message
            print("Sending:", reply)  # Print message being sent
            conn.sendall(reply.encode("utf-8"))  # Echo message back to the client
        except:
            break  # Handle exceptions and exit loop

    print("Connection lost")
    conn.close()  # Close connection when the client disconnects

# Main loop to accept multiple clients
while True:
    conn, addr = s.accept()  # Accept new client connection
    print("Connected to", addr)
    start_new_thread(threaded_client, (conn,))  # Start a new thread for each client
