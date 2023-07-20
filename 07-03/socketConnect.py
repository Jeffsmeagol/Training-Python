import socket
'''
s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host,port))

print('Waiting for connection..')
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got connection from', addr)
  conn.send('Server sssssssssaying hi'.encode())
  conn.close()
'''
def server_program():
  host = '0.0.0.0'
  port = 5000
  server_socket = socket.socket()
  server_socket.bind((host, port))
  print('waiting......')
  server_socket.listen(2)
  conn, address = server_socket.accept()
  print('connection from: ' + str(address))
  while True:
    data = conn.recv(1024).decode()
    if not data:
      break
    print('from connected user: ' + str(data))
    data = input(' -> ')
    conn.send(data.encode())
  conn.close()
if __name__ == '__main__':
  server_program()