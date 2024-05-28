from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, marca, modelo,portas) -> None:
        super().__init__(marca, modelo)
        self.qtd_portas = portas
        
        
    def __str__(self) -> str:
        return str(super().__str__()) + " ,Qtd portas:"+self.qtd_portas
    
    
    
