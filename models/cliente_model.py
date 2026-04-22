from config.configuracao import Configuracao
from database_app.services.cliente_service import localiza_cliente

class ClienteModel:
    @staticmethod
    def validar_clientes(client_id_request, client_secret_request):
        client_id_db, client_secret_db = localiza_cliente(client_id_request)
        print('Secret request',client_id_request)
        print('secret db      ',client_secret_db)
        return (
            client_id_request == client_id_db and
            client_secret_request == client_secret_db
        )