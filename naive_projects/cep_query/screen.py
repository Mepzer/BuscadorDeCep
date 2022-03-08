import PySimpleGUI as sg
from logging import getLogger
from typing import NamedTuple
from sys import stdout

from cep_api import CepApi, CepInfo


log = getLogger(__name__)


class Dimension(NamedTuple):
    width: int
    height: int

    def take_piece(self, percent: float) -> NamedTuple:
        w, h = int(self.width * percent), int(self.height * percent)
        return Dimension(w, h)


class Screen:
    def __init__(
        self,
        width: int, height: int,
        title: str,
        cep_api: CepApi,
    ):
        self.title = title
        self.cep_api = cep_api
        self.dimension = Dimension(width, height)
        self.layout = [
            [sg.Text('cep'), sg.Input(size=(25, 0), key='CEP')],
            [sg.Button('Buscar')],
            [self.build_console_element()],
        ]

    def build_console_element(self) -> sg.Element:
        # dimensão do console vai ser 40% da janela
        return sg.Output(size=self.dimension.take_piece(0.4))

    def take_cep_info(self, cep: str) -> CepInfo:
        if not self.cep_api:
            raise AttributeError(f"É necessário um objeto {type(CepInfo)}")

        return self.cep_api.query_cep_data(cep)

    def init_ui(self):
        win = sg.Window(
            self.title,
            self.layout,
            size=self.dimension,
            resizable=True)

        while True:
            try:
                event, values = win.Read()
                if event in (sg.WINDOW_CLOSED, 'Exit', 'Quit'):
                    return

                cep_info = self.take_cep_info(values)
                print(cep_info)

            except Exception as err:
                print(err.__class__, err.args)


def build_screen(dimension: tuple, title: str = "Cep Info") -> Screen:
    return Screen(
        *dimension,
        title=title,
        cep_api=CepApi(),
    )
