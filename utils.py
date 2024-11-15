import os 

def create_folder(log_folder): 
    log_file = os.path.join(log_folder, 'server.log')
    os.makedirs(log_folder, exist_ok=True)
