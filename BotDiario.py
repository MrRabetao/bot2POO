from Robot import Robot

class BotDiario(Robot):
    
    def __init__(self):
        super().__init__()
        self.problemas = ['Você percebe as letras se moverem enquanto tenta ler alguma palavra?', 'Você presencia fadiga ocular em si mesmo que o faz efetuar piscadas excessivas dos olhos e sentir dores de cabeça?',
                          'Você sente que tem dificuldades para entender uma mensagem que lhe é passada através de uma fala?','Você possui alguma dificuldade com lateralidade, isto é, qual a direita e esquerda?',
                          'Você costuma trocar as letras no momento da leitura ou escrita?']
        self.regs = []
        
    def versionamentoLog(self, versao, log):
        self.versao = versao
        self.log = log
    
    def registroProb(self,idProb, comentario):
        self.regs.append([idProb, comentario])
        
    def getProb(self, idProb):
        return self.problemas[idProb]
    
    def getRegs0(self, idRegs):
        return self.regs[idRegs][0]
    def getRegs1(self, idRegs):
        return self.regs[idRegs][1]
        