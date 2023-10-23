import socket

def cliente_connect():
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('192.168.2.11',7777))
    cliente.close()

cliente_connect()