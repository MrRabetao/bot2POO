class Relatorio:

    def __init__(self,nome,botDiario):
        self.nome = nome
        self.botDiario = botDiario
        self.rel = f"Nome: {nome}\nProblema registrados: \n"

        for i in range (len(self.botDiario.regs)):
            index = self.botDiario.getRegs0(i)
            coment = self.botDiario.getRegs1(i)
            self.rel = self.rel + (self.botDiario.getProb(index)+"\n"+f"Comentario: {coment}"+"\n\n")

        with open("relatorio.txt","w",encoding="utf-8") as arquivo:
            arquivo.write(self.rel)

    

