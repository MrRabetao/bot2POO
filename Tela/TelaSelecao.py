#from BotDiario import BotDiario
from PySimpleGUI import PySimpleGUI as tela

class TelaSelecao:
    
    def __init__(self):
        tela.theme('DarkBlue15')
        self.fechado = False
    
    def layoutMenu(self):
        self.layout = [
            [tela.Button('Registrar Dificuldade'), tela.Button('Caça Palavras'), tela.Button('Gerar Relatorio')]   
        ]
        return tela.Window('Selecao',layout = self.layout, finalize=True)
        
    def iniciarTela(self):
        tela.popup('Selecione o que quer começar agora.')
        self.layoutMenu = self.layoutMenu()


    
    

        while True: 
            janela, eventos, valores = tela.read_all_windows()
            
            if janela == self.layoutMenu and eventos == tela.WINDOW_CLOSED:
                self.layoutMenu.close()
                self.fechado = True
                break
   
            if janela == self.layoutMenu and eventos == 'Registrar Dificuldade':
                self.layoutMenu.close()
                return 1
            if janela == self.layoutMenu and eventos == 'Caça Palavras':
                self.layoutMenu.close()
                return 2
            if janela == self.layoutMenu and eventos == 'Gerar Relatorio':
                tela.popup("Seu arquivo foi gerado na raiz deste programa, com o nome 'relatorio.txt'")
                self.layoutMenu.close()
                return 3