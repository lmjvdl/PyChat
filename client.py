import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # دریافت پیام از سرور
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # اگر پیامی دریافت نشد، سرور قطع شده است
                print("Disconnected from server.")
                break
            print(message)
        except:
            # اگر خطایی رخ داد، سرور قطع شده است
            print("Disconnected from server.")
            break

def send_messages(client_socket):
    while True:
        # دریافت پیام از کاربر
        message = input()
        
        # ارسال پیام به سرور
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            # اگر ارسال ناموفق بود، سرور قطع شده است
            print("Failed to send message.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'
    port = 12345
    
    # اتصال به سرور
    client_socket.connect((host, port))
    print("Connected to server.")
    
    # ایجاد thread برای دریافت پیام‌ها
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    # ایجاد thread برای ارسال پیام‌ها
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()