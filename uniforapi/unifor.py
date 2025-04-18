from uniforapi.authentication.requester import Requester


class UniforClient:
    def __init__(self, matricula: str, senha: str):
        
        self.token = Requester.post_unifor_auth(self, matricula = matricula, senha = senha)
        # print(self.token)
        if not self.token or not self.token.uni_token:
            raise Exception("Erro ao autenticar")

    def acessar_inicio(self):
        Requester.acessar_pagina_inicial(self, self.token)
       
    # Métodos futuros
