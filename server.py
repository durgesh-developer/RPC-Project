import socket
import threading
import logging

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE=1024

def handle_client(conn, addr):
  """Handles communication with a connected client."""
  logger = logging.getLogger(f'Client {addr}')
  buffer = ''  
  while True:
    try:
      
      data = conn.recv(BUFFER_SIZE).decode()
      if not data:
        break
      buffer += data
      if '\n' in buffer:
        message, buffer = buffer.split('\n', 1)
        message, task_number = message.rsplit(' ', 1)
        if message == 'close' or message == 'quit':
         conn.sendall("Connection terminated by client.".encode())
         break
        else:
         converted_message = convert_message(message, int(task_number))
         conn.sendall(converted_message.encode())
         buffer='' # clear buffer
    except Exception as e:
      logger.error(f"Error processing message: {e}")
      conn.sendall(f"Server error: {str(e)}".encode())
      break

def convert_message(message, task_number):
  """Converts the message based on the task number."""
  if task_number == 1:
    return message.lower()
  elif task_number == 2:
    return message.upper()
  elif task_number == 3:
    return message.title()
  else:
    return f"Invalid task number: {task_number}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  print('Server listening on', (HOST, PORT))
  while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    # Create a new thread to handle each client connection
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
