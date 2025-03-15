import socket
import threading

# لیست برای نگهداری کلاینت‌های متصل
clients = []

def broadcast(message, sender_socket):
    # ارسال پیام به همه کلاینت‌ها به جز فرستنده
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # اگر ارسال ناموفق بود، کلاینت را از لیست حذف کنید
                clients.remove(client)

def handle_client(client_socket, addr):
    # اضافه کردن کلاینت به لیست
    clients.append(client_socket)
    print(f"Connection from {addr} accepted. Total clients: {len(clients)}")
    
    while True:
        try:
            # دریافت داده از کلاینت
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                # اگر داده‌ای دریافت نشد، کلاینت قطع شده است
                break
            
            print(f"Received from {addr}: {data}")
            
            # ارسال پیام به همه کلاینت‌ها
            broadcast(f"Client {addr}: {data}", client_socket)
        except:
            # اگر خطایی رخ داد، کلاینت قطع شده است
            break
    
    # حذف کلاینت از لیست و بستن سوکت
    clients.remove(client_socket)
    client_socket.close()
    print(f"Connection from {addr} closed. Total clients: {len(clients)}")

def start_server():
    # ایجاد سوکت
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # آدرس و پورت سرور
    host = '127.0.0.1'
    port = 12345
    
    # اتصال سوکت به آدرس و پورت
    server_socket.bind((host, port))
    
    # گوش دادن به اتصالات ورودی
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")
    
    while True:
        # پذیرش اتصال از کلاینت
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} accepted :)")
        
        # ایجاد یک thread جدید برای مدیریت کلاینت
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()