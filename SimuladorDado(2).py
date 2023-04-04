#Criando janela
#Lendo valores da tela
# Utilizando os valores
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]

    def Iniciar(self):
        #Criando Janela
        self.janela = sg.Window('Simulador De Dado',layout=self.layout)
        ###Ler valores da tela
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print("Agradecemos a sua participação ")
            else:
                print('Porfavor Digite Sim(s) ou Não(n): ')
        except:
                print('Ocorreu um erro com a sua resposta! ') 

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()


