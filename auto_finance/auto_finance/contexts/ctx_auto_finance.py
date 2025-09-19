from datetime import datetime

from auto_finance.controllers.ctr_auto_finance import AutoFinanceCtr

class AutoFinanceCtx:
    def __init__(self):
        self._ctr_auto_finance = AutoFinanceCtr()
        
    def teste(self): 
        self._ctr_auto_finance.definir_saudacao()
        self._ctr_auto_finance.iniciar_interface()
