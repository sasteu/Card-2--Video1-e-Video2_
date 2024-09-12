class Contador:
    contador = 0  # Atributo de classe 
    
    def inst(self):  # Método de instância 
        return 'Estou bem!' 
    
    @classmethod
    def incremento(cls):  # Método de classe
        cls.contador += 1  
        return cls.contador  
 
    @classmethod
    def decremento(cls):  # Método de classe 
        cls.contador -= 1  
        return cls.contador  

    @staticmethod
    def mais_um(n):  # Método estático 
        return n + 1 
    
    
c1 = Contador()  # Cria uma instância da classe 'Contador'.
print(c1.inst())  # Chama o método de instância 'inst' e exibe a mensagem "Estou bem!".

print(Contador.incremento())  # Chama o método de classe 'incremento' diretamente pela classe e incrementa o 'contador'.
print(c1.incremento())  # Chama o método 'incremento' pela instância c1 (mas opera no atributo de classe, compartilhado).
print(c1.decremento())  
print(c1.incremento())  
print(c1.decremento()) 
print(Contador.mais_um(99))  # Chama o método estático 
