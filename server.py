import socket
import signal
import sys
import argparse

def receive_data_from_client(protocol):
    server_ip = '0.0.0.0'
    server_port = 8432

    if protocol == 'u':
        # Create a socket object for UDP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    elif protocol == 't':
        # Create a socket object for TCP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        print("Invalid protocol. Use 'u' for UDP or 't' for TCP.")
        return

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_ip, server_port))

    if protocol == 't':
        # Listen for incoming connections (TCP only)
        server_socket.listen(5)

    print(f"Server listening on {protocol.upper()}...")

    def signal_handler(sig, frame):
        print('Shutting down server...')
        server_socket.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            if protocol == 'u':
                # Receive data (UDP)
                data, addr = server_socket.recvfrom(1024)
                print(f"Received from {addr}: {data.decode()}")
            elif protocol == 't':
                # Accept incoming connection (TCP)
                client_socket, addr = server_socket.accept()
                data = client_socket.recv(1024).decode()
                print(f"Received from {addr}: {data}")
                client_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start a server with specified protocol.')
    parser.add_argument('-p', '--protocol', choices=['u', 't'], default='u', help='Protocol to use (u for UDP, t for TCP)')
    args = parser.parse_args()

    receive_data_from_client(args.protocol)