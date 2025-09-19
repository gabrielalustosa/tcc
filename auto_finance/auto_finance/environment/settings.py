from os import getlogin
from pathlib import Path
from platform import system
import socket

# SISTEMA:
SISTEMA = system()
USUARIO_SIST_OPER = getlogin()
COMANDO_FECHAR_CMD = 'taskkill /f /im cmd.exe'
IP_MAQUINA = socket.gethostbyname(socket.gethostname())

# PASTAS:
_PASTA_PROJETO = str(Path.cwd()).replace('\\', '/')
_NOME_PROJETO = _PASTA_PROJETO.split('/')[-1]
PASTA_LOGS = f'{_PASTA_PROJETO}/logs'
PASTA_DATABASE = f'{_PASTA_PROJETO}/{_NOME_PROJETO}/environment/database'
PASTA_DATABASE_JSON = f'{_PASTA_PROJETO}/{_NOME_PROJETO}/environment/database/json'

# DEFINIÇÕES:
TEMPO_ARMZ_LOGS = 6
TIPO_TEMPO_ARMZ_LOGS = 'meses'
TEAMS_WEBHOOK = 'https://confederacaosicredi.webhook.office.com/webhookb2/81e64cc5-e3b2-4af0-9297-2516635790ef@3223964c-6e1f-48ba-b705-423351281a8c/IncomingWebhook/f7000e4b99a144829b6511786d82eb31/0625c27b-613f-4899-b3e1-aa01e741f046/V2A8habKzgxfr4RiDN1gOd1L6FFHCBIazvi-_SuAkDdLM1'
