import PySimpleGUI as sg
from datetime import datetime

class AutoFinanceCtr:
    def __init__(self):
        self._nome = ""
        self._saudacao = ""

    def definir_saudacao(self):
        hora = datetime.now().hour
        if 5 <= hora < 12:
            self._saudacao = "Bom dia!"
        elif 12 <= hora < 18:
            self._saudacao = "Boa tarde!"
        else:
            self._saudacao = "Boa noite!"

    def iniciar_interface(self):
        layout = [
            [sg.Text(f'{self._saudacao} ao Auto_Finance!')],
            [sg.Text("Informe seu nome para personalizar sua planilha:")],
            [sg.InputText(key='nome')],
            [sg.Button('Continuar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Auto_Finance - Assistente Financeiro', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            elif event == 'Continuar':
                self._nome = values['nome']
                sg.popup(f"Perfeito, {self._nome}! Vamos começar a organizar suas finanças.")
                break

        window.close()