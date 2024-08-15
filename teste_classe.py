import os
os.system('cls' if os.name == 'nt' else 'clear')


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Criando instâncias da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Agora carro1 e carro2 são instâncias da classe Carro
print(carro1.marca)  # Saída: Toyota
print(carro2.modelo)  # Saída: Civic
