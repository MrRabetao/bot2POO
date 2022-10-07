from Robot import Robot

class BotDiario(Robot):
    
    def __init__(self):
        super().__init__()
        self.problemas = ['PROBLEMAS GERAIS', 'LEITURA/ESCRITA', 'FLUÊNCIA LEITORA','DIFICULDADES NA MEMORIZAÇÃO','LATERALIDADE']
        self.regs = []
        
    def versionamentoLog(self, versao, log):
        self.versao = versao
        self.log = log
    
    def registroProb(self,idProb):
        self.regs.append(idProb)
        
    def getProb(self, idProb):
        return self.problemas[idProb]
        
