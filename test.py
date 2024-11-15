import socket 
import yaml

# Configuración del cliente
def main():  
    config        = yaml.safe_load(open("parameters.yaml"))
    HOST          = config['host']
    PORT          = config['port']
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect((HOST, PORT))
    print('Prueba1, mensaje Hola :\n')
    client_socket.sendall('Hola'.encode())
    data = client_socket.recv(1024)
    print("Respuesta del servidor:", data.decode())

    print('Prueba2, Mensaje DESCONEXION:\n')
    client_socket.sendall('DESCONEXION'.encode())
    data = client_socket.recv(1024)
    print("Respuesta del servidor:", data.decode())

    client_socket.close()
    print("Conexión cerrada.")

if __name__ == '__main__':
    main() 