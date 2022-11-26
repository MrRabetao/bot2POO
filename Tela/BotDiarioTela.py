#from BotDiario import BotDiario
from PySimpleGUI import PySimpleGUI as tela


class BotDiarioTela:

    def __init__(self, botDiario):
        self.botDiario = botDiario
        tela.theme('DarkBlue15')

    def layoutMenu(self):
        self.layout = [
            [tela.Radio(self.botDiario.getProb(0), 'gp1', key='op0')],
            [tela.Radio(self.botDiario.getProb(1), 'gp1', key='op1')],
            [tela.Radio(self.botDiario.getProb(2), 'gp1', key='op2')],
            [tela.Radio(self.botDiario.getProb(3), 'gp1', key='op3')],
            [tela.Radio(self.botDiario.getProb(4), 'gp1', key='op4')],
            [tela.Button('Prosseguir'), tela.Button(
                'Sobre'), tela.Button('Sair')]

        ]
        return tela.Window('Diario', layout=self.layout, finalize=True)

    def comentario(self):
        self.layout = [
            [tela.Text('Adicione um comentário sobre o problema:')],
            [tela.Text('Você também pode deixar em branco.')],
            [tela.Input(key='coment')],
            [tela.Button('Submeter')]
        ]
        return tela.Window('Comentarios', layout=self.layout, finalize=True)

    def iniciarTela(self):
        tela.popup(
            'Selecione a classe do problema que mais se encaixa na dificuldade encontrada.')
        self.layoutMenu = self.layoutMenu()
        self.comentario = self.comentario()
        self.comentario.hide()
        self.escolha = 0
        
        while True:
            janela, eventos, valores = tela.read_all_windows()

            if janela == self.layoutMenu and eventos == tela.WINDOW_CLOSED:
                self.layoutMenu.close()
                break

            if janela == self.comentario and eventos == tela.WINDOW_CLOSED:
                self.comentario.close()
                break
            
            

            if janela == self.layoutMenu and eventos == 'Prosseguir':
                if valores['op0'] == True:
                    tela.popup(self.botDiario.dicas(0))
                    self.layoutMenu.hide()
                    self.comentario.un_hide()
                    self.escolha = 0

                if valores['op1'] == True:
                    tela.popup(self.botDiario.dicas(1))
                    self.comentario.un_hide()
                    self.layoutMenu.hide()
                    self.escolha = 1
                if valores['op2'] == True:
                    tela.popup(self.botDiario.dicas(2))
                    self.comentario.un_hide()
                    self.layoutMenu.hide()
                    self.escolha = 2
                if valores['op3'] == True:
                    tela.popup(self.botDiario.dicas(3))
                    self.comentario.un_hide()
                    self.layoutMenu.hide()
                    self.escolha = 3
                if valores['op4'] == True:
                    tela.popup(self.botDiario.dicas(4))
                    self.comentario.un_hide()
                    self.layoutMenu.hide()
                    self.escolha = 4

            if janela == self.comentario and eventos == 'Submeter':
                self.comentario.hide()
                if self.escolha == 0:
                    self.botDiario.registroProb(0, valores['coment'])
                    self.comentario.hide()
                    self.layoutMenu.un_hide()
                if self.escolha == 1:
                    self.botDiario.registroProb(1, valores['coment'])
                    self.comentario.hide()
                    self.layoutMenu.un_hide()
                if self.escolha == 2:
                    self.botDiario.registroProb(2, valores['coment'])
                    self.comentario.hide()
                    self.layoutMenu.un_hide()
                if self.escolha == 3:
                    self.botDiario.registroProb(3, valores['coment'])
                    self.comentario.hide()
                    self.layoutMenu.un_hide()
                if self.escolha == 4:
                    self.botDiario.registroProb(4, valores['coment'])
                    self.comentario.hide()
                    self.layoutMenu.un_hide()

            if janela == self.layoutMenu and eventos == 'Sobre':
                tela.popup(self.botDiario.mostrarDados())

            if janela == self.layoutMenu and eventos == 'Sair':
                self.layoutMenu.close()
                break
