class FuncNaoEncontrada(Exception):
    def __init__(self):
        super().__init__('Não foi encontrada a função para esse objeto')
