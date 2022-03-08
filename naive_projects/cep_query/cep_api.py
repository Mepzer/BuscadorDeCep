from dataclasses import dataclass, asdict
from requests import get as http_get
from sys import stdout


@dataclass(init=True)
class CepInfo:
    cep: str = str()
    logradouro: str = str()
    complemento: str = str()
    bairro: str = str()
    localidade: str = str()
    uf: str = str()
    ibge: str = str()
    gia: str = str()
    ddd: str = str()
    siafi: str = str()

    def __str__(self) -> str:
        _str = str()
        for k, v in asdict(self).items():
            _str += f"[ {k.upper()} = {v.upper() or '*'} ]\n"

        return _str


class CepApi:
    @classmethod
    def query_cep_data(cls, cep: str) -> CepInfo:
        response = http_get(cls.take_endpoint(cep))

        if response.status_code in range(0, 200):
            print('Sucesso!', file=stdout)
        elif response.status_code > 300:
            print(f'Erro {response.status_code}', file=stdout)
            return CepInfo()

        return CepInfo(**response.json())

    @classmethod
    def take_endpoint(cls, cep: str) -> str:
        return f'https://viacep.com.br/ws/{cep}/json/'
