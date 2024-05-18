import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
BUFFER_SIZE=1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while True:
    # Get message and task number from user
    message = input("Enter message: ")
    task_number = input("Enter task number (1: lowercase, 2: uppercase, 3: sentence case): ")
    data = f"{message} {task_number}\n".encode()
    s.sendall(data)
    data = s.recv(BUFFER_SIZE)
    print(data.decode())
    if data.decode().startswith("Connection terminated"):
      break

print('Closing socket')
