import socket

HOST = '127.0.0.1'
PORT = 65432

def run_client():
    # Створюємо клієнтський сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Підключаємось до сервера

        # Відправляємо повідомлення
        message = "Привіт від клієнта!"
        s.sendall(message.encode('utf-8'))

        # Читаємо відповідь
        data = s.recv(1024)
        print("Отримано відповідь:", data.decode('utf-8'))

if __name__ == "__main__":
    run_client()
