import socket 
import yaml

# Configuración del cliente
def main():  
    config        = yaml.safe_load(open("parameters.yaml"))
    HOST          = config['host']
    PORT          = config['port']
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect((HOST, PORT))
    print("Conectado al servidor. Puedes enviar mensajes. Escribe 'DESCONEXION' para salir.")
    while True: 
        mensaje = input('Mensaje para el servidor: ')  
        if mensaje:
            client_socket.sendall(mensaje.encode())
            data = client_socket.recv(1024)
            print("Respuesta del servidor:", data.decode())
            if mensaje == 'DESCONEXION':
                print("Desconectándose del servidor...")
                break
        else:
            print('Mensaje vacío. Intenta de nuevo.')
    client_socket.close()
    print("Conexión cerrada.")

if __name__ == '__main__':
    main() 