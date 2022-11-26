class Robot:
    
    def __init__(self):
        self.nome = "Ubuntu"
        self.tipo = "Virtual"
        self.tarefa = ("O Bot Anamnese tem como intuito ajudar pessoas que\ncarregam o transtorno da dislexia ou que possui dúvidas sobre o assunto.\n"+
        "Com um funcionamento simples e direto, ele vai\nentregar ao usuário um apanhado de dicas sobre a dislexia acompanhado\n"+
        "de uma espécie de diário e um relatório e, ao final,\njuntando tudo isso, o usuário terá uma anamnese que pode auxiliá-lo\n"+
        "enquanto ao que ele deve dizer ao médico.")
    
    def versionamentoLog(self, versao, log):
        self.versao = versao
        self.log = log
    
    def addSugestao(self, sugestao):
        self.sugestao = sugestao
        
    def dicas(self, idDicas):
        
        if idDicas == 0:
            return "Segundo o artigo do professor Jonh Stein, esquiadores e atiradores de elite sabem que o uso de óculos amarelos pode melhorar sua sensibilidade ao contraste em condições de 'branco'. Isso ocorre porque a visualização através de filtros amarelos faz com que as pupilas se dilatem. Fazer com que algumas crianças visualizem o texto por meio desses filtros amarelos pode ajudar muitas a melhorar sua leitura."       
        elif idDicas == 1:
            return "Segundo o artigo do professor Jonh Stein, quando damos óculos azuis às crianças, parecemos estar estimulando seu sistema de excitação ativando essas células de melanopsina, dar às crianças filtros azuis profundos apropriados poderia melhorar sua atenção e melhorar sua leitura em mais de nove meses em três meses. Além disso, melhoraram o padrão de sono das crianças, pois ajudaram a sincronizar esse relógio hipotalâmico. Além disso, eles pareciam melhorar as dores de cabeça das crianças, provavelmente pelo mesmo mecanismo. Assim, os filtros azuis muitas vezes podem ajudar as crianças a se adequarem, ativando o sistema de melanopsina para melhorar a atenção e a excitação."      
        elif idDicas == 2:
            return "A sensibilidade de muitas pessoas com dislexia às modulações de frequência e amplitude é significativamente reduzida. Segundo o artigo do professor Jonh Stein, vários grupos de pessoas afetadas por esse distúrbio também mostraram que o treinamento musical ou rítmico melhora a sensibilidade FM e AM dos disléxicos e pode ajudá-los a melhorar suas habilidades fonológicas."        
        elif idDicas == 3:
            return "No ato de ler usamos o movimento de direita para a esquerda com a cabeça e o olhar o tempo todo, agora mesmo você está executando essa movimentação ao percorrer este artigo, a linha acaba e você precisa direcionar os olhos para a esquerda e acompanhar a linha de baixo. Um nervo ocular é responsável por estes movimentos e crianças que têm dificuldade neste sentido podem estar precisando treiná-lo."      
        elif idDicas == 4:
            return "A troca de letras é dita normal na fase da alfabetização, porém se a mesma for recorrente deve-se procurar especialistas. Então é muito importante que os pais busquem profissionais especializados e experientes, para que não haja confusão no diagnóstico. Se uma criança produz textos com trocas de letras na escrita, a dislexia não é a única possibilidade, existe ainda outro transtorno que pode ser o causador da dificuldade, a disortografia."
        
        return "invalido"
    
    def mostrarDados(self):
        sobre =f"O nome do nosso grupo é "+self.nome
        sobre+=f"!\nEste e todos os bots deste trabalho são do tipo "+self.tipo
        sobre+=f".\nE a tarefa deste bot é:\n"+self.tarefa
        return (sobre)
    
    