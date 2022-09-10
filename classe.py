# Desenvolvedora: Ana Vitoria S. Luz
# Atividade didática com intuito de fixar conteúdo sobre POO
# luiza code 5 edição.

                         # Criação da classe base

class Faccoes: 
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
                         # todas as faccoes herdam da classe base através de herança
        
class Abnegacao(Faccoes):
    def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)
 
class Audacia(Faccoes):
    def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)
        
class Amizade(Faccoes):
   def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)

class Franqueza(Faccoes):
     def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)

class Erudicao(Faccoes):
    def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)
        
        
                            #encapsulamento
      
        
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

    acesso = membro.acessar_clube("Quatro")
    print(acesso)

    acesso = membro.acessar_clube("Tris")
    print(acesso)
            
    
    # instanciando e printando o resultado.

    #PrimeiraFaccao= Audacia('audacia', 'coragem','ana vitoria')
    #print(f'o nome da faccao é {PrimeiraFaccao.nome}, o seu valor é {PrimeiraFaccao.valor} e o seu participante principal é {PrimeiraFaccao.participante}')
    
    #SegundaFaccao = Abnegacao ('Abnegacao', 'altruismo', 'Tris')
    #print(f'o nome da faccao é {SegundaFaccao.nome}, o seu valor é {SegundaFaccao.valor} e o seu participante principal é {SegundaFaccao.participante}')
