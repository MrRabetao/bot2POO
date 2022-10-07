from BotDiario import BotDiario
from PySimpleGUI import PySimpleGUI as tela

class BotDiarioTela:
    
    def __init__(self, botDiario):
        self.botDiario = botDiario
        tela.theme('Reddit')
    
    def layoutMenu(self):
        self.layout = [
            [tela.Radio(self.botDiario.getProb(0),'gp1', key='op0')],
            [tela.Radio(self.botDiario.getProb(1),'gp1', key='op1')],
            [tela.Radio(self.botDiario.getProb(2),'gp1', key='op2')],
            [tela.Radio(self.botDiario.getProb(3),'gp1', key='op3')],
            [tela.Radio(self.botDiario.getProb(4),'gp1', key='op4')],
            [tela.Button('Prosseguir')]
            
        ]
        return tela.Window('Diario',layout = self.layout, finalize=True)
        
    def iniciarTela(self):
        tela.popup('Selecione a classe do problema que mais se encaixa na dificuldade encontrada.')
        self.layoutMenu = self.layoutMenu()

        while True: 
            janela, eventos, valores = tela.read_all_windows()
            
            if janela == self.layoutMenu and eventos == tela.WINDOW_CLOSED:
                break
   
            if janela == self.layoutMenu and eventos == 'Prosseguir':
                if valores['op0'] == True:
                    tela.popup(self.botDiario.dicas(0))
                    self.botDiario.registroProb(0)
                if valores['op1'] == True:
                    tela.popup(self.botDiario.dicas(1))
                    self.botDiario.registroProb(0)
                if valores['op2'] == True:
                    tela.popup(self.botDiario.dicas(2))
                    self.botDiario.registroProb(0)
                if valores['op3'] == True:
                    tela.popup(self.botDiario.dicas(3))
                    self.botDiario.registroProb(0)
                if valores['op4'] == True:
                    tela.popup(self.botDiario.dicas(4))
                    self.botDiario.registroProb(0)
                