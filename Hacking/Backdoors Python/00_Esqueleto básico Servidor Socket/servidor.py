import socket

def upserver():
    global server
    global ip # Obtiene la dirección IP que se conecto, será una tupla.
    global target # Objeto de la conexión, interactuar para recibir y enviar datos.
    
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tipo de conex
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Opciones de conexion
        server.bind(('192.168.2.11',7777)) #Colocar nuestra IP y puerto para comunicarnos.
        server.listen(1) #El valor de 1 es porque deja el servidor en escuchar
        print('[*] Servidor en escucha, esperando conexiones..')

        target, ip = server.accept()
        print("[+] Conexion exitosa.")
        print("[+] Conexion recibida de: " + str(ip[0]))



    except ConnectionError as e:
        print('[-] Error, '+ e)     


if __name__ == '__main__':
    upserver()
    server.close()