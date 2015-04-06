# encoding: utf-8
import random
random.randrange(start=-1,stop=1)

class Pydaline(object):
    
    def __init__(self):
        """
        Inicializa o Pydaline
        """
        self.pesos = []
        self.saidas_desejadas = []
        self.entradas = []
        self.taxa_aprendizado = 0.01
        self.debug = True
        self.theta = .7
        self.epocas = 0
        self.erro_global = 1

    def set_debug(self,debug=True):
        """
        Se ativado, ele mostrará as mensagens de treinamento
        """
        self.debug = debug
        
    def set_entradas(self,entradas):
        """
        Aplica as entradas fornecidas e reajusta o número de pesos
        """
        if len(entradas) >= 2:
            #cria novos pesos
            self.entradas = entradas
            self.pesos = []
            for i, entrada in enumerate(entradas[0]):
                self.pesos.append(random.random())

    def get_saida(self, entrada):
        if not self.pesos:
            raise RuntimeError(u'Pesos não configurados')
        if len(self.pesos) != len(entrada):
            raise RuntimeError(u'Vetor de pesos diferente do vetor de entrada')

        self.entradas = [entrada]
        return self.ativacao(0)

    def set_saidas_desejadas(self,saidas):
        """
        Ajusta as as saídas desejadas necessárias para treinar o neuronio
        """
        if len(saidas) >= 2:
            self.saidas_desejadas = saidas

    def criterio_parada(self):
        """
        Critério de parada. Sobrescreva para mudar.
        """
        return (self.epocas==100)
    
    def somatorio(self, num_entrada):
        """
        Faz o somatório do produto de cada entrada com seu respectivo peso
        """
        somatorio = 0
        for i,entrada in enumerate(self.entradas[num_entrada]):
            somatorio += self.pesos[i]* entrada
        return somatorio
    
    def ativacao(self, num_entrada):
        """
        Função de ativação. Sobrescreva se quiser uma diferente.
        """
        somatorio = self.somatorio(num_entrada)
        if somatorio>=self.theta:
            return 1
        elif somatorio<-self.theta:
            return -1
        return 0
    
    def aprender(self):
        """
        Realiza o treinamento por épocas.
        """
        if len(self.saidas_desejadas) != len(self.entradas):
            raise RuntimeError("Whoops! O número de entradas é diferente do número de saídas desejadas.")
        while self.erro_global != 0:
            if self.criterio_parada():
                print "Não convergiu. Critério de parada atingido. Pesos:", self.pesos, "Erro global:", self.erro_global
                break
            self.epocas += 1
            if self.debug: 
                print "Iniciando epoca: ",self.epocas,". Erro Global:",self.erro_global
            self.erro_global = 0
            self.treina()
            
            
    def treina(self):
        """
        Percorre as entradas, calcula as saídas e passa o erro para a função de ajuste
        """
        for i, entrada in enumerate(self.entradas): #treina o nuronio para cada entrada
            saida = self.ativacao(i)
            erro = self.saidas_desejadas[i]-saida
            self.erro_global += abs(erro)
            if self.debug:
                print "\n Entradas",entrada
                print " Saida desejada: ",self.saidas_desejadas[i]
                print " Saida encontrada: ",saida
                print " Erro: ",erro
                print " Pesos:",self.pesos
            self.ajusta_pesos(erro, i)

    def ajusta_pesos(self, erro, num_entrada):
        """
        Principal função: realiza o ajuste de pesos (aprendizado) quando houver erro.
        """
        if erro !=0:
            plen = len(self.pesos)
            for j in range(0,plen):
                x = self.entradas[num_entrada][j]
                self.pesos[j] = self.pesos[j] + self.taxa_aprendizado*erro*x
            if self.debug: 
                print " Pesos atualizados:",self.pesos
    
    def teste_manual(self):
        """
        Teste individual
        """
        print "######### Prompt de teste #########"
        r = "s"
        entradas_fornecidas = []
        while r=="s":
            for i in range(len(self.entradas[0])):
                print "Entrada ",i
                entradas_fornecidas.append(float(raw_input(": ")))
            self.entradas[0] = entradas_fornecidas
            if self.debug: print entradas_fornecidas
            print "Saida: ",self.ativacao(0)
            r = raw_input("Continuar testando?")
            entradas_fornecidas = []
