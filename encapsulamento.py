class Clube_Divergente:
    def __init__(self, lider):
        self.lider = lider
    
    def get_fundador(self):
        return 'Tris'
    
    def __mostrar_acesso_clube(self):
        return "Você é um membro, pode entrar!"

    def acessar_clube(self, membro):
        if membro == "Tris":
            return self.__mostrar_acesso_clube()
        
        return "Voce não é um membro e não tem acesso!"
    
membro = Clube_Divergente(['Tris'])

acesso = membro.acessar_clube("Ana")
print(acesso)

acesso = membro.acessar_clube("Tris")
print(acesso)