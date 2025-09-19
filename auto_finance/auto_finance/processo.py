"""
Onde se os passos (steps) da automação
"""

from loguru import logger

from auto_finance._set_step import definir_steps
from auto_finance.tools.exceptions import FuncNaoEncontrada
from auto_finance.tools.support import logging
from auto_finance.contexts.ctx_auto_finance import AutoFinanceCtx

class Processo:
    def __init__(self):
        self._processo_ctx = AutoFinanceCtx()

        logging.formatar_log()
        logging.deletar_arquivos_log()

    def iniciar(self):
        detalhes = ''
        lista_steps = definir_steps(self._processo_ctx)  # TODO - mudar parâmetro

        try:
            for step in lista_steps:
                try:
                    continuar, detalhes = getattr(step.objeto, step.funcao)()
                except AttributeError:
                    raise FuncNaoEncontrada

                if not continuar:
                    logger.error(
                        f'Virou pendente pelo motivo = {detalhes}'
                    )  # TODO - mudar texto se achar necessário

                    break

        except FuncNaoEncontrada:
            detalhes = f'Não encontrada a a função "{step.funcao}" no step: {step.nome}'
            logger.error(detalhes)

        except Exception as erro:
            detalhes = f'Erro desconhecido: {erro=}'
            logger.critical(detalhes)

        finally:
            logger.debug('Atualizando informações tarefa')