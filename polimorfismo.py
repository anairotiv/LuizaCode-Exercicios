class Pessoa:
    def __init__(self):
        pass
    
    def Pessoa_indefinida(self):
        return 'Indefinida'
    
class Transformar(Pessoa):
    def __init__(self, another):
        self.another = another
        super().__init__()
 
    def Pessoa_indefinida(self):
        return f"O quatro pode se transformar na {self.another}."
    
Pessoa1 = Transformar('Tris')
print(Pessoa1.Pessoa_indefinida())