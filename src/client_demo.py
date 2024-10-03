from ssh_stream import Client, Server

client = Client(ip='localhost', port=9999)

if not client.connect():
    print("Failed to connect")
    exit(1)

data = "Hello, world!"
i = 0

for i in range(len(data)):
    if not client.send(data[i]):
        print("Failed to send data")
        break

client.close()



