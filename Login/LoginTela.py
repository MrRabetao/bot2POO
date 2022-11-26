from PySimpleGUI import PySimpleGUI as tela


class LoginTela:
    
    def __init__(self, login):
        self.login = login
        tela.theme('DarkBlue15')
    
    def layoutInicial(self):
        self.layout = [
            [tela.Text('Senha: '), tela.Input(key = 'password',password_char="*")],
            [tela.Button('Entrar'), tela.Button('Trocar Senha')]
            
        ]
        return tela.Window('Login',layout = self.layout, finalize=True)
    
    def alterarSenha(self):
        self.layout = [
            [tela.Text('Senha anterior: '), tela.Input(key = 'oldPass',password_char="*")],
            [tela.Text('Nome: '), tela.Input(key = 'nome')],
            [tela.Text('Senha: '), tela.Input(key = 'password',password_char="*")],
            [tela.Button('Alterar')]
        ]
        return tela.Window('Alterar Usuário',layout = self.layout, finalize=True)

        
    def iniciarTela(self):
        tela.popup('A senha mestra padrão do sistema é "1", e o nome é Usuário\nCaso queira mudar, apenas aperte em Trocar Senha!')
        self.layoutInicial = self.layoutInicial()
        self.alterarSenha = self.alterarSenha()
        self.alterarSenha.hide()
        
        while True:
            janela, eventos, valores = tela.read_all_windows()
            
            if janela == self.alterarSenha and eventos == tela.WINDOW_CLOSED:
                break
            if janela == self.layoutInicial and eventos == tela.WINDOW_CLOSED:
                break
 
            
            if janela == self.layoutInicial and eventos == 'Entrar':
                self.login.entrar(valores['password'])
                if self.login.logado == True:
                    tela.popup('Seja Bem Vindo!')
                    self.alterarSenha.close()
                    self.layoutInicial.close()
                    break
                else:
                    tela.popup('Senha errada, tente novamente')
                    
            if janela == self.layoutInicial and eventos == 'Trocar Senha':
                self.layoutInicial.hide()
                self.alterarSenha.un_hide()
                
            if janela == self.alterarSenha and eventos == 'Alterar':
                msg, alterado = self.login.alterarSenha(valores['oldPass'],valores['nome'],valores['password'])
                tela.popup(msg)
                if alterado:
                    self.alterarSenha.hide()
                    self.layoutInicial.un_hide()