import socket
import threading

# Dictionary to store usernames and their corresponding client sockets
clients = {}

def broadcast(message, sender_username):
    # Send the message to all clients except the sender
    for username, client_socket in clients.items():
        if username != sender_username:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                # If sending fails, remove the client from the dictionary
                del clients[username]

def handle_client(client_socket, addr):
    # Receive the username from the client
    username = client_socket.recv(1024).decode('utf-8')
    print(f"Connection from {addr} accepted. Username: {username}")
    
    # Add the client to the dictionary
    clients[username] = client_socket
    
    # Notify all clients about the new connection
    broadcast(f"{username} joined the chat!", username)
    
    while True:
        try:
            # Receive a message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # If no message is received, the client has disconnected
                break
            
            print(f"Received from {username}: {message}")
            
            # Broadcast the message to all clients with the username
            broadcast(f"{username}: {message}", username)
        except:
            # If an error occurs, the client has disconnected
            break
    
    # Remove the client from the dictionary and close the socket
    del clients[username]
    client_socket.close()
    broadcast(f"{username} left the chat.", username)
    print(f"Connection from {username} closed.")

def start_server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Server address and port
    host = '127.0.0.1'
    port = 12345
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")
    
    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} accepted :)")
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()