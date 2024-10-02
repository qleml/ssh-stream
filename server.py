import socket
import signal
import sys

def receive_data_from_client():
    server_ip = '0.0.0.0'
    server_port = 8432

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening...")

    def signal_handler(sig, frame):
        print('Shutting down server...')
        server_socket.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            # Accept incoming connection
            client_socket, addr = server_socket.accept()

            # Receive data
            data = client_socket.recv(1024).decode()
            print(f"Received: {data}")

            # Close client connection
            client_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    receive_data_from_client()