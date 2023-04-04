#simulador de dado
#simular o uso de um dado, gerando valores de 1 a 6
import random
import PySimpleGUI

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de girar novamente?\n'
  
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'nao' or resposta == 'n':
                print("Agradecemos a sua participação \n")
            else:
                print('Porfavor Digite Sim(s) ou Não(n): \n')
        except:
                print('Ocorreu um erro com a sua resposta! \n') 

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()










