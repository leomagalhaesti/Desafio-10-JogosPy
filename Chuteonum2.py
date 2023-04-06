import random
import PySimpleGUI as sg

class ChuteONumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(39, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chute!')],
            [sg.Output(size=(39, 10))]
        ]
        #Criar janela
        self.janela = sg.Window('Chute o Numero', layout)
        self.GerarNumeroAleatorio()
        while True:
            ######
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            #fazer algo cm valores
            elif evento == 'Chute!':
                try:
                    valor_do_chute = int(valores['ValorChute'])
                except ValueError:
                    print('Chute apenas numeros entre 1 a 100')
                    continue
                if valor_do_chute > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                elif valor_do_chute < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                if valor_do_chute == self.valor_aleatorio:
                    sg.popup_ok('Parabens, você acertou!')
                    break
        self.janela.close()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
