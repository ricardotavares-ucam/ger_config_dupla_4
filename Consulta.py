class Consulta:
    def __init__(self, data_con, historico):
        self.data_con = data_con
        self.historico = historico

        def get_data_con(self):
            return self.data_con
        
        def set_data_con(self, data_con):
            self.data_con = data_con
        
        def get_historico(self):
            return self.historico
        
        def set_historico(self, historico):
            self.historico = historico
        
        def list_con(self):
            return "Listar todas as consultas de um determinado tratamento"
        
        def ver_con(self):
            return "Ver uma consulta específica"
        
        def reg_con(self):
            return "Marcar uma nova consulta"