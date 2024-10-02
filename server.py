import socket

def receive_data_from_client():
    server_ip = '0.0.0.0'
    server_port = 9999

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening...")

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")

        # Receive data
        data = client_socket.recv(1024).decode()
        print(f"Received: {data}")

        # Close client connection
        client_socket.close()

if __name__ == "__main__":
    receive_data_from_client()
