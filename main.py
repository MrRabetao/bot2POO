from Login.Login import Login
from Login.LoginTela import LoginTela
from BotDiario import BotDiario
from Tela.BotDiarioTela import BotDiarioTela
from Tela.TelaSelecao import TelaSelecao
from Tela.TelaCacaPalavras import TelaCacaPalavras
from Relatorio import Relatorio

login = Login()
loginTela = LoginTela(login)
loginTela.iniciarTela()
botDiario = BotDiario()
telaSelecao = TelaSelecao()

if login.logado == True:
    while telaSelecao.fechado == False:
        telaSelecao = TelaSelecao()
        selecao = telaSelecao.iniciarTela()
        if selecao == 1:
            botDiarioTela = BotDiarioTela(botDiario)
            botDiarioTela.iniciarTela()
        elif selecao == 2:
            telaCaca = TelaCacaPalavras()
            telaCaca.iniciarTela()
        elif selecao == 3:
            relatorio = Relatorio(botDiario.nome,botDiario)