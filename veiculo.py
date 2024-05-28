class Veiculo:
    
    def __init__(self,marca,modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
        
    @property
    def ligado(self):
        return "Ligado" if self._ligado else "Desligado"
  
    def __str__(self) -> str:
        return f'Marca:{self.marca+", Modelo:"+self.modelo+" ,Estado:"+ self.ligado}'