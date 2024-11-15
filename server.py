import socket
import logging
import yaml
import os
from utils import create_folder

def main():  
    config     = yaml.safe_load(open("parameters.yaml"))
    HOST       = config['host']
    PORT       = config['port']
    USE_LOG    = config['use_log']
    LOG_FOLDER = config['log_folder'] 
    LOG_FILE   = config['log_file']
    DEBUG      = config['debug']
    if USE_LOG:    
        create_folder(LOG_FOLDER)
        handlers = [logging.FileHandler(f'{LOG_FOLDER}/{LOG_FILE}'),logging.StreamHandler()] if DEBUG else [logging.FileHandler(f'{LOG_FOLDER}/{LOG_FILE}')]
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=handlers)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))  # Asocia la IP y el puerto al socket
        server_socket.listen()            # Pone el servidor en modo de escucha

        if USE_LOG: logging.info(f"Servidor TCP iniciado en {HOST}:{PORT}, en espera de conexiones...")

        while True:
            # Espera a que un cliente se conecte
            client_socket, client_address = server_socket.accept()
            if USE_LOG: logging.info(f"Conexión aceptada de {client_address}")
            with client_socket:
                while True:
                    try:
                        # Recibe datos del cliente
                        data = client_socket.recv(1024)
                        if not data:
                            if USE_LOG:logging.warning(f"Conexión cerrada inesperadamente por el cliente {client_address}")
                            break

                        mensaje = data.decode()
                        if USE_LOG: logging.info(f"Mensaje recibido del cliente {client_address}: {mensaje}")

                        if mensaje == "DESCONEXION":
                            if USE_LOG: logging.info(f"Cliente {client_address} ha solicitado la desconexión")
                            response = "Desconexión confirmada. Adiós!"
                            client_socket.sendall(response.encode()) 

                        response = mensaje.upper()
                        client_socket.sendall(response.encode())
                        if USE_LOG: logging.info(f"Respuesta enviada al cliente {client_address}: {response}")

                    except Exception as e:
                        if USE_LOG: logging.error(f"Error al comunicarse con el cliente {client_address}: {e}")
                        break
                if USE_LOG:logging.info(f"Conexión con {client_address} finalizada")
    



if __name__ == '__main__':
    main()