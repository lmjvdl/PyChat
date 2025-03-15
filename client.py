import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive a message from the server
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # If no message is received, the server has disconnected
                print("Disconnected from server.")
                break
            print(message)  # Display the received message
        except:
            # If an error occurs, the server has disconnected
            print("Disconnected from server.")
            break

def send_messages(client_socket):
    while True:
        # Get a message from the user
        message = input()
        
        # Send the message to the server
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            # If sending fails, the server has disconnected
            print("Failed to send message.")
            break

def start_client():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Server address and port
    host = '127.0.0.1'
    port = 12345
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Get the username from the user
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))  # Send the username to the server
    
    print("Connected to server. You can start chatting!")
    
    # Create a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    # Create a thread to send messages to the server
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()