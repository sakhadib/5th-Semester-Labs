import socket
import time

target_host = "0.0.0.0"  # Corrected the variable name from 'targer_host'
target_port = 9998 

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))
message = "dfgjhdakdhgfghujikljfdhgujikrehgijhresuighuirsehguiohreuighuireshguiorthesuoighrduisofhjgouireshguihrfdhuhguihjkhjihiuhuihui"
i = 0

try:
    while True:
        i = i + 1    
        client.send(message.encode()) 

        # Receive some data
        response = client.recv(4096)
        print(f"Received [{i}]:", response.decode())
        print()
        time.sleep(1)

finally:
    client.close()  # Ensure the socket is closed when done

# import time
# for i in range(5):
#     print(f"\rProgress: {i+1}/5", end="")
#     time.sleep(1)




# import socket

# targer_host = "192.168.0.100"
# target_port = 9998

# # create a socket object
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # connect the client
# client.connect((targer_host, target_port))

# # send some data
# client.send(b"hello!!!")

# # receive some data
# response = client.recv(4096)

# print(response.decode())
# client.close()
