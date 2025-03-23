import socket

# Define a Network class for the client
class Network:
    def __init__(self):
        # Create a TCP client socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.8"  # Server IP
        self.port = 5560  # Port to connect to
        self.addr = (self.server, self.port)  # Tuple containing server address
        self.id = self.connect()  # Attempt to connect to the server
        print(self.id)  # Print the connection message

    # Connect to the server
    def connect(self):
        try:
            self.client.connect(self.addr)  # Connect to the server
            return self.client.recv(2048).decode()  # Receive and return server's response
        except:
            return "Connection Failed"  # Return error message if connection fails

    # Send data to the server and receive response
    def send(self, data):
        try:
            self.client.send(str.encode(data))  # Send encoded data to server
            return self.client.recv(2048).decode()  # Receive and return server response
        except socket.error as e:
            print(e)  # Print error if any occurs

# Create a client instance and test sending messages
n = Network()
print(n.send("HII"))  # Send "HII" and print server response
print(n.send("Working"))  # Send "Working" and print server response
