from datetime import date, datetime
from os import listdir, remove, stat
from sys import stderr
from typing import Literal

from dateutil.relativedelta import relativedelta
from loguru import logger

from auto_finance.environment.settings import (
    PASTA_LOGS,
    TEMPO_ARMZ_LOGS,
    TIPO_TEMPO_ARMZ_LOGS,
)


def _get_save_path():
    data = date.today().strftime('%Y-%m-%d')
    nome_arquivo = f'{data}.txt'

    return f'{PASTA_LOGS}/{nome_arquivo}'

def formatar_log():
    logger.remove()
    formato_log = (
        '{time:HH:mm:ss} | <level>{level:<8}</level> | {message:<65} | {file}-{line}'
    )
    logger.add(sink=stderr, format=formato_log, level='INFO')


def _deletar_logs_antigos(
    arquivo: str, tempo_armazenagem: int, tipo_tempo: Literal['dias', 'meses']
):
    infos_gerais_arquivo = stat(arquivo)

    data_arquivo = datetime.fromtimestamp(infos_gerais_arquivo.st_ctime)
    hoje = datetime.now()

    if tipo_tempo == 'meses':
        dif = relativedelta(hoje, data_arquivo).months
    else:
        dif = relativedelta(hoje, data_arquivo).days

    if dif > tempo_armazenagem:
        remove(arquivo)

def deletar_arquivos_log():
    for arquivo in listdir(PASTA_LOGS):
        path_arquivo = f'{PASTA_LOGS}/{arquivo}'
        if arquivo.endswith('.txt'):
            _deletar_logs_antigos(
                path_arquivo,
                tempo_armazenagem=TEMPO_ARMZ_LOGS,
                tipo_tempo=TIPO_TEMPO_ARMZ_LOGS,
            )
        else:
            _deletar_logs_antigos(path_arquivo, tempo_armazenagem=6, tipo_tempo='meses')
