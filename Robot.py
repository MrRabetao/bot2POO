class Robot:
    
    def __init__(self):
        self.nome = "Ubutu"
        self.tipo = "Virtual"
        self.tarefa = "O Bot Anamnese tem como intuito ajudar pessoas que\ncarregam o transtorno da dislexia ou que possui dúvidas sobre o assunto.\n",
        "Com um funcionamento simples e direto, ele vai\nentregar ao usuário um apanhado de dicas sobre a dislexia acompanhado\n",
        "de uma espécie de diário e um relatório e, ao final,\njuntando tudo isso, o usuário terá uma anamnese que pode auxiliá-lo\n",
        "enquanto ao que ele deve dizer ao médico."
    
    def versionamentoLog(self, versao, log):
        self.versao = versao
        self.log = log
    
    def addSugestao(self, sugestao):
        self.sugestao = sugestao
        
    def dicas(self, idDicas):
        if idDicas == 0:
            return "dica1"
        
        elif idDicas == 1:
            return "dica1"
        
        elif idDicas == 2:
            return "dica2"
        
        elif idDicas == 3:
            return "dica3"
        
        elif idDicas == 4:
            return "dica4"
        
        return "invalido"
    
    
