import PySimpleGUI as sg
import json
import requests

class Tela:
    def __init__(self):

        layout = [
            [sg.Text('cep'),sg.Input(size=(25, 0), key='CEP')],
            [sg.Button('Buscar')],
            [sg.Output(size=(40, 10))]
        ]

        self.tela = sg.Window('Busca de CEP',layout)

    def consultar(self,cep):

        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
            print('Sucesso')
        elif url.status_code == 400:
            print('Erro 400')

        endereco = url.json()

        return endereco

    def telaIni(self):

        while True:
            self.button, self.values = self.tela.Read()
            try:
                codcep = self.consultar(self.values['CEP'])
                for k, v in codcep.items():
                    print(k.upper(), ':',v)
            except:
                print('Error')

sp = Tela()
sp.telaIni()





