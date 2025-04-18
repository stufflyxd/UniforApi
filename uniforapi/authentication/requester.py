import json
from typing import Optional

import requests
from uniforapi.authentication.constants import AUTHORIZATION_HEADER, URL_AUTH, URL_INICIO
from uniforapi.models.token import TokenUnifor


class Requester:
    # Essa variável pode ser do tipo X, ou pode ser None.
    # Optional[TokenUnifor] -> TokenUnifor | None
    def post_unifor_auth(self, matricula: str, senha: str) -> Optional[TokenUnifor]:
        """
        Realiza a autenticação com a API da Unifor e retorna um objeto TokenUnifor
        com os dados de autenticação.

        Args:
            matricula (str): Matrícula do aluno.
            senha (str): Senha de acesso.

        Returns:
            Optional[TokenUnifor]: Objeto com os tokens de autenticação, ou None
            em caso de falha.
        """

        self.session = requests.Session()

        self.session.headers.update({
            'Content-type': 'application/json',
            'Authorization': AUTHORIZATION_HEADER
        })

        payload = {
            "user": matricula,
            "password": senha,
        }

        headers = {
            "Content-type": "application/json",
            "Authorization": AUTHORIZATION_HEADER,
        }

        try:
            # Retorna em um dicionario
            self.resposta = self.session.post(
                URL_AUTH, headers=headers, data=json.dumps(payload), proxies= {'http': None,'https': None}
            )
            self.resposta.raise_for_status()

            # Verifica se a resposta é JSON antes de tentar decodificar

            if "application/json" in self.resposta.headers.get("Content-Type", ""):
                json_data = self.resposta.json()
                return TokenUnifor(json_data)

            else:
                print("Resposta não está em formato JSON")
                return None

        except requests.HTTPError as http_err:
            print(f"Erro HTTP: {http_err} | Código: {self.resposta.status_code}")
        except requests.RequestException as req_err:
            print(f"Erro de conexão: {req_err}")
        except ValueError as json_err:
            print(f"Erro ao decodificar JSON: {json_err}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

        return None



    def acessar_pagina_inicial(self, token: TokenUnifor) -> Optional[requests.Response]:
        """
        Acessa a página inicial da plataforma da Unifor usando o token
        de autenticação fornecido.

        Args:
            token (TokenUnifor): Token válido contendo os cookies de autenticação.

        Returns:
            Optional[requests.Response]: Resposta HTTP se a requisição for
            bem-sucedida, ou None em caso de erro.
        """
        try:
            self.resposta = requests.get(URL_INICIO, cookies=token.as_cookie(), proxies={'http': None, 'https': None})

            # Verifica os status e leva uma exceção
            self.resposta.raise_for_status()

        # Relativo à exceção acima
        except requests.exceptions.HTTPError as e:
            print(f'Erro no HTTP: {e}')

        except requests.exceptions.RequestException as e:
            print(f'Erro na requisição (genérico): {e}')