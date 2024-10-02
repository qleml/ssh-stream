import socket

def send_data_to_server(data):
    server_ip = '192.168.1.66'
    server_port = 9999

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client_socket.connect((server_ip, server_port))

        # Send data
        client_socket.sendall(data.encode())

        # Close connection
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        data = "Sensor data or image"
        send_data_to_server(data)
