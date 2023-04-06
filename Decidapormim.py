import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você deveria saber',
            'Não acho uma boa escolha',
            'Sim, inclusive ja passou da hora. '
        ]

    def Iniciar (self):
        #Layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        #Criar janela
        self.janela = sg.Window('Decida por Mim!',layout)
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WIN_CLOSED:
                break
            if eventos == 'Decida por mim':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()


