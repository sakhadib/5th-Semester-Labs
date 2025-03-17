import paramiko
import sys
import select
import socket
import threading

ssh_user = "sakhadib" 
ssh_password = "1928" 
remote_host = "127.0.0.1"
remote_port = 8080
local_port = 3000

def forward_tunnel(local_port, remote_host, remote_port, transport):
    class SubHandler(paramiko.Channel):
        def __init__(self, channel):
            super().__init__(channel)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind(("127.0.0.1", local_port))
            self.sock.listen(1)

        def run(self):
            while True:
                client_sock, _ = self.sock.accept()
                remote = transport.open_channel('direct-tcpip', (remote_host, remote_port), client_sock.getpeername())
                if remote is None:
                    print("Failed to open channel.")
                    return
                while True:
                    r, w, x = select.select([client_sock, remote], [], [])
                    if client_sock in r:
                        data = client_sock.recv(1024)
                        if len(data) == 0:
                            break
                        remote.send(data)
                    if remote in r:
                        data = remote.recv(1024)
                        if len(data) == 0:
                            break
                        client_sock.send(data)

    transport.request_port_forward("", local_port)
    SubHandler(transport).run()

def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print("Connecting to SSH server...")
    client.connect("127.0.0.1", username=ssh_user, password=ssh_password)
    transport = client.get_transport()

    print(f"Setting up tunnel from 127.0.0.1:{local_port} to {remote_host}:{remote_port}...")
    forward_tunnel(local_port, remote_host, remote_port, transport)
    
    client.close()

if __name__ == "__main__":
    main()
