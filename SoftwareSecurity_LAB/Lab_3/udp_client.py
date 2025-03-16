import socket
target_host = "8.8.8.8"
target_port = 53

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
query = b'\xaa\xbb\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' \
        + b'\x07example\x03com\x00\x00\x01\x00\x01'
client.sendto(query, (target_host, target_port))

# receive some data
data, addr = client.recvfrom(512)

print(data)
client.close()