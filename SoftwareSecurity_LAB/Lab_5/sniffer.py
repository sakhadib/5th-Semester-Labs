from scapy.all import sniff, IP
import socket

# Resolve IP address of google.com
google_ip = socket.gethostbyname("google.com")
print(f"IP address of google.com: {google_ip}")

# Define a callback function to process the sniffed packet
def packet_callback(packet):
    if IP in packet and packet[IP].src == google_ip:
        print("Packet sniffed from google.com:")
        print(packet.summary())
        return True  

# Sniff one packet from google.com
print("Sniffing one packet from google.com...")
sniff(filter=f"src host {google_ip}", prn=packet_callback, count=1)