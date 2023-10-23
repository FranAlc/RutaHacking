import socket
import os
import subprocess


def consola():
    print("[*] Digite 'exit()' para salir.")
    sh = os.getcwd()
    cliente.send(sh)
    while True:
        if sh == 'exit()':
            break
        else:
            respuesta = cliente.recv(1024)
            print(respuesta.decode('utf-8'))
            
def cliente_connect():
    global cliente
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('192.168.2.11',7777))
        print("[+] Ha ingresado al servidor")
        consola()
        cliente.close()
    except ConnectionError as e:
        print("[-] Error de conexion, "+ e)

cliente_connect()