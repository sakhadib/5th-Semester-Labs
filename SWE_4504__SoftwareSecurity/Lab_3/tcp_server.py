import socket
import threading

ip = '0.0.0.0'
port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"[*] Listening on {ip}:{port}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        i = 0
        while True:  # Loop to continuously handle messages
            try:
                i = i + 1
                request = sock.recv(1024)  # Receive data from the client
                if not request:  # If request is empty, the client has disconnected
                    print("[*] Client has disconnected.")
                    break
                print(f"[*] Received [{i}]: {request.decode()}\n")
                sock.send(b"ACK")  # Send an acknowledgment back to the client
            except Exception as e:
                print(f"[*] An error occurred: {e}")
                break  # Exit the loop on any error

if __name__ == "__main__":
    main()


# import socket
# import threading

# ip = '0.0.0.0'
# port = 9998

# def main():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((ip, port))
#     server.listen(5)
#     print(f"[*] Listening on {ip}:{port}")

#     while True:
#         client, address = server.accept()
#         print(f"[*] Accepted connection from {address[0]}:{address[1]}")
#         client_handler = threading.Thread(target=handle_client, args=(client,))
#         client_handler.start()
    
# def handle_client(client_socket):
#     with client_socket as sock:
#         request = sock.recv(1024)
#         print(f"[*] Received: {request.decode()}\n")
#         sock.send(b"ACK")
        
# if __name__ == "__main__":
#     main()