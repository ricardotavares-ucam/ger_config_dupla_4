class Tratamento:

    def __init__(self, data_ini, data_fin):
        self.data_ini = data_ini
        self.data_fin = data_fin

        def get_data_ini(self):
            return self.data_ini

        def get_data_fin(self):
            return self.data_fin

        def set_data_ini(self, data_ini):
            self.data_ini = data_ini
        
        def set_data_fin(self, data_fin):
            self.data_fin = data_fin
        
        def vis_trat(self):
            return "Visualizar todos os tratamentos já realizados por um Animal"
        
        def con_Trat(self):
            return "Consultar um determinado tratamento"

        def reg_Trat(self):
            return "Abrir um novo tratamento"