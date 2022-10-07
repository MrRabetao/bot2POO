class Login:
    
    def __init__(self):
        self.logado = False
        self.password = "1"
        self.nome = 'Usuário'
        
    def criarUser(self, nome, password):
        ret = "Usuário criado!"
        if nome != "":
            self.nome = nome
            if len(password)>3:
                self.password = password
            else:
                ret = "Defina uma Senha válida!"
        else:
            ret = "Defina um nome!"
     
        return ret
        
    def entrar(self, password):
        if password == self.password:
            self.logado = True
        else:
            self.logado = False
            
    def alterarSenha(self, oldPass, nome, password):
        if oldPass == self.password:
            ret = self.criarUser(nome,password)
            if ret == "Usuário criado!":
                return "Dados alterados!", True
            else:
                return ret, False
        else:
            return "Senha Incorreta!", False
            
    def sair(self):
        self.logado = False


            
        
        
        
        

        
    