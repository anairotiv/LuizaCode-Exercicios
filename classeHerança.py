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

# class Erudicao(Faccoes):
   # def __init__(self, nome, valor, participante):
       # self.participante = participante
       # super().__init__(nome, valor)
        
        
    

        PrimeiraFaccao = Audacia('audacia', 'coragem','ana vitoria')
        print(f'o nome da faccao é {PrimeiraFaccao.nome}, o seu valor é {PrimeiraFaccao.valor} e o seu participante principal é {PrimeiraFaccao.participante}')
        
        SegundaFaccao = Abnegacao ('Abnegacao', 'altruismo', 'Tris')
        print(f'o nome da faccao é {SegundaFaccao.nome}, o seu valor é {SegundaFaccao.valor} e o seu participante principal é {SegundaFaccao.participante}')

        TerceiraFaccao = Amizade('audacia', 'coragem','ana vitoria')
        print(f'o nome da faccao é {TerceiraFaccao.nome}, o seu valor é {TerceiraFaccao.valor} e o seu participante principal é {TerceiraFaccao.participante}')
        
        QuartaFaccao = Franqueza('audacia', 'coragem','ana vitoria')
        print(f'o nome da faccao é {QuartaFaccao.nome}, o seu valor é {QuartaFaccao.valor} e o seu participante principal é {QuartaFaccao.participante}')
        
       # QuintaFaccao = Erudicao('bla bla', 'bla', 'blabla')
       #print(f'o nome é {QuintaFaccao.nome}, o seu valor é {QuintaFaccao.valor} e o seu participante principal é {QuintaFaccao.participante} ')