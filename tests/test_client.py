import json
from uniforapi.api.inicio import acessar_pagina_inicial
from uniforapi.models.token import TokenUnifor



def test_acessar_pagina_inicial_real():
    token_real = TokenUnifor()