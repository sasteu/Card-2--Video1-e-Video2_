class Carro:  # Define a classe 'Carro'.
    def __init__(self):  # Método construtor que inicializa a velocidade do carro.
        self.__velocidade = 0  # Atributo privado que armazena a velocidade.

    @property
    def velocidade(self):  # Propriedade para acessar a velocidade do carro de forma controlada.
        return self.__velocidade  
        
    def acelerar(self):  # Método que aumenta a velocidade em 5 unidades.
        self.__velocidade += 5
        return self.__velocidade  
        
    def frear(self):  # Método que diminui a velocidade em 5 unidades.
        self.__velocidade -= 5
        return self.__velocidade  
    
class Uno(Carro):  # Define a classe 'Uno', que herda da classe 'Carro'.
    pass  

class Ferrari(Carro):  # Define a classe 'Ferrari', que herda da classe 'Carro'.
    def acelerar(self):  # Sobrescreve o método 'acelerar' da classe 'Carro'.
        super().acelerar()  
        return super().acelerar()  


c1 = Carro()
print(c1.acelerar())  
print(c1.acelerar())  
print(c1.acelerar())  
print(c1.frear())    
print(c1.frear())     
print(c1.frear())     


c2 = Uno()
print(c2.acelerar())  
print(c2.acelerar())
print(c2.acelerar())
print(c2.frear())
print(c2.frear())
print(c2.frear())


c3 = Ferrari()
print(c3.acelerar())  
print(c3.acelerar())  
print(c3.acelerar())  
print(c3.frear())     
print(c3.frear())     
print(c3.frear())     
