


class TokenUnifor:
    def __init__(self, data=None):

        data = data or {}
        # {
        #   "data": {
        #       "accessToken": "...",
        #       "uniforToken": "...",
        #       "refreshtoken": "..."
        #   }
        # }

        # Seguro, recebe um dicionário vazio como padrão se não existir
        token_data = data.get('data', {})
        self.uni_token = token_data.get('uniforToken')  # Unico necessário
        self.access_token = token_data.get('accessToken')
        self.refresh_token = token_data.get('refreshToken')

    def as_cookie(self) -> dict:
        return {'X-UNIFOR-API-Token': self.uni_token} if self.uni_token else {}
