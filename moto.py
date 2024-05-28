from veiculo import Veiculo

class Moto(Veiculo):
    
    def __init__(self, marca, modelo,tipo) -> None:
        super().__init__(marca, modelo)
        self.tipo = tipo
        
    def __str__(self) -> str:
        return super().__str__()+ f" ,Tipo:{self.tipo}"
    
    
