from Login.Login import Login
from Login.LoginTela import LoginTela
from BotDiario import BotDiario
from Tela.BotDiarioTela import BotDiarioTela

login = Login()
loginTela = LoginTela(login)
loginTela.iniciarTela()
if login.logado == True:
    botDiario = BotDiario()
    botDiarioTela = BotDiarioTela(botDiario)
    botDiarioTela.iniciarTela()
