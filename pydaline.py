# -*- coding: utf-8 -*-
import random
random.randrange(start=-1,stop=1)
class Pydaline:
    
    def __init__(self):
        """
        Inicializa o Pydaline
        """
        self.pesos = []
        self.saidas_desejadas = []
        self.entradas = []
        self.theta = 0.7 # inteligente bagaraio
        self.alpha = 0.9 #taxa de aprendizado
        self.debug = True
        self.epocas = 0
        self.erroGlobal = 1 # assume que inicia sem treinamento

    def setDebug(self,debug=True):
        """
        Se ativado, ele mostrará as mensagens de treinamento
        """
        self.debug = debug
        
    def setEntradas(self,entradas):
        """
        Aplica as entradas fornecidas e reajusta o número de pesos
        """
        if entradas.__len__()>=2:
            #cria novos pesos
            self.entradas = entradas
            self.pesos = []
            for i in range(0,entradas[0].__len__()):
                self.pesos.append(random.random())

    def setSaidasDesejadas(self,saidas):
        """
        Ajusta as as saídas desejadas necessárias para treinar o neuronio
        """
        if saidas.__len__()>=2:
            self.saidas_desejadas = saidas

    def criterio_parada(self):
        """
        Critério de parada. Sobrescreva para mudar.
        """
        return (self.epocas==100) #treinamento máximo em 100 épocas
    
    def somatorio(self,numEntrada):
        """
        Faz o somatório do produto de cada entrada com seu respectivo peso
        """
        somatorio = 0
        for i in range(0,self.entradas[numEntrada].__len__()):
            somatorio += self.pesos[i]*self.entradas[numEntrada][i]
        return somatorio
    
    def ativacao(self,numEntrada):
        """
        Função de ativação. Sobrescreva se quiser uma diferente.
        """
        somatorio = self.somatorio(numEntrada)
        if somatorio>=self.theta:
            return 1
        elif somatorio<-self.theta:
            return -1
        return 0
    
    def aprender(self):
        """
        Realiza o treinamento por épocas.
        """
        if self.saidas_desejadas.__len__()!=self.entradas.__len__():
            raise RuntimeError("Whoops! O número de entradas é diferente do número de saídas desejadas.")
        while self.erroGlobal != 0 and not self.criterio_parada():
            self.epocas += 1
            if self.debug: print "Iniciando epoca: ",self.epocas,". Erro Global:",self.erroGlobal
            self.erroGlobal = 0
            self.treina()
            
            
    def treina(self):
        """
        Percorre as entradas, calcula as saídas e passa o erro para a função de ajuste
        """
        for i in range(0,self.entradas.__len__()): #treina o nuronio para cada entrada
            ativacao = self.ativacao(i)
            erro = self.saidas_desejadas[i]-ativacao
            self.erroGlobal += erro.__abs__()
            if self.debug:
                print " Entradas",self.entradas[i]
                print " Saida desejada: ",self.saidas_desejadas[i]
                print " Saida encontrada: ",ativacao
                print " Erro: ",erro
                print " Pesos:",self.pesos
            self.ajusta_pesos(erro,i)

    def ajusta_pesos(self,erro,numEntrada):
        """
        Principal função: realiza o ajuste de pesos (aprendizado) quando houver erro.
        """
        if erro !=0:
            plen = self.pesos.__len__()
            for j in range(0,plen):
                self.pesos[j] = self.pesos[j] + self.alpha*erro*self.entradas[numEntrada][j]
            if self.debug: print " Pesos atualizados:",self.pesos
    
    def obter_resposta_para_entrada(self, entrada):
        if entrada.__len__() != self.entradas[0].__len__():
            raise RuntimeError("A entrada deve ter o mesmo tamanho das usadas no treinamento")
        self.entradas.append(entrada)
        resultado = self.ativacao(self.entradas.__len__()-1)
        self.entradas.pop()
        return resultado

    def teste_manual(self):
        """
        Teste individual
        """
        print "######### Prompt de teste #########"
        r = "s"
        entradas_fornecidas = []
        while r=="s":
            for i in range(self.entradas[0].__len__()): # for(i=0;i<numEntradas;i++)
                print "Entrada ",i
                entradas_fornecidas.append(int(raw_input(": ")))
            self.entradas[0] = entradas_fornecidas
            if self.debug: print entradas_fornecidas
            print "Saida: ",self.ativacao(0)
            r = raw_input("Continuar testando?")
            entradas_fornecidas = []


def main():
    ##############################################################
    digito_a0 = [1,1,1,1,1,
                 1,1,0,1,1,
                 1,0,0,0,1,
                 1,1,1,1,1,
                 1,0,0,0,1]

    digito_a1 =  [0,1,1,1,0,
                  1,1,0,1,1,
                  1,0,0,0,1,
                  1,1,1,1,1,
                  1,0,0,0,1]

    digito_b0 = [1,1,1,1,0,
                 1,0,0,0,1,
                 1,1,1,1,1,
                 1,0,0,0,1,
                 1,1,1,1,0]

    digito_b1 = [1,1,1,1,1,
                 1,0,0,0,1,
                 1,1,1,1,1,
                 1,0,0,0,1,
                 1,1,1,1,1]

    digito_c0 = [1,1,1,1,1,
                 1,0,0,0,0,
                 1,0,0,0,0,
                 1,0,0,0,0,
                 1,1,1,1,1]

    digito_c1 = [0,1,1,1,1,
                 1,1,0,0,0,
                 1,0,0,0,0,
                 1,1,0,0,0,
                 0,1,1,1,1]

    digito_d0 = [1,1,1,1,0,
                 1,0,0,1,1,
                 1,0,0,0,1,
                 1,0,0,1,1,
                 1,1,1,1,0]

    digito_d1 = [1,1,1,1,1,
                 1,0,0,1,1,
                 1,0,0,0,1,
                 1,0,0,1,1,
                 1,1,1,1,1]

    digito_e0 = [1,1,1,1,1,
                 1,0,0,0,1,
                 1,1,1,1,1,
                 1,0,0,0,0,
                 1,1,1,1,1]

    digito_e1 = [1,1,1,1,0,
                 1,0,0,0,1,
                 1,1,1,1,0,
                 1,0,0,0,0,
                 1,1,1,1,0]

    digito_f0 = [1,1,1,1,1,
                 1,0,0,0,0,
                 1,1,1,1,1,
                 1,0,0,0,0,
                 1,0,0,0,0]

    digito_f1 = [1,1,1,1,1,
                 1,0,0,0,0,
                 1,0,0,0,0,
                 1,1,1,1,1,
                 1,0,0,0,0]

    digito_g0 = [1,1,1,1,1,
                 1,0,0,0,0,
                 1,1,1,1,1,
                 1,0,0,0,1,
                 1,1,1,1,1]

    digito_g1 = [1,1,1,1,0,
                 1,0,0,0,0,
                 1,1,1,1,0,
                 1,0,0,0,1,
                 0,1,1,1,0]

    digito_h0 = [1,1,1,1,1,
                 1,0,0,0,0,
                 1,1,1,1,1,
                 1,0,0,0,1,
                 1,1,1,1,1]

    digito_h1 = [1,0,0,0,1,
                 1,0,0,0,1,
                 1,1,1,1,1,
                 1,0,0,0,1,
                 0,1,1,1,1]

    digito_h1 = [1,0,0,0,1,
                 1,0,0,0,1,
                 1,0,0,0,1,
                 1,1,1,1,1,
                 0,1,1,1,1]

    digito_i0 = [1,1,1,1,1,
                 0,0,1,0,0,
                 0,0,1,0,0,
                 0,0,1,0,0,
                 1,1,1,1,1]

    digito_i1 = [0,0,1,0,0,
                 0,0,0,0,0,
                 0,0,1,0,0,
                 0,0,1,0,0,
                 0,1,1,1,0]

    digito_j0 = [0,0,1,1,1,
                 0,0,0,0,1,
                 1,0,0,0,1,
                 1,0,0,0,1,
                 1,1,1,1,1]

    digito_j1 = [0,0,0,0,1,
                 0,0,0,0,0,
                 0,0,0,0,1,
                 0,1,0,0,1,
                 0,1,1,1,1]

    digito_k0 = [1,0,0,1,1,
                 1,0,1,0,0,
                 1,1,0,0,0,
                 1,0,1,0,0,
                 1,0,0,1,1]

    digito_k1 = [0,0,0,0,0,
                 1,0,1,0,0,
                 1,1,0,0,0,
                 1,0,1,0,0,
                 1,0,0,1,0]
    # a = [-1,-1,-1,-1] => neuron_1 = -1, neuron_2 =-1, neuron_3 = -1, etc
    # b = [-1,-1,-1, 1]
    # c = [-1,-1, 1,-1]
    # d = [-1,-1, 1, 1]
    # e = [-1, 1,-1,-1]
    # f = [-1, 1,-1, 1]
    # g = [-1, 1, 1,-1]
    # h = [-1, 1, 1, 1]
    # i = [ 1,-1,-1,-1]
    # j = [ 1,-1,-1, 1]
    # k = [ 1,-1, 1,-1]
    # l = [ 1,-1, 1, 1]
    # m = [ 1, 1,-1,-1]
    # n = [ 1, 1,-1, 1]
    # o = [ 1, 1, 1,-1]
    # p = [ 1, 1, 1, 1]

    entradas = [digito_a0,digito_a1,
            digito_b0,digito_b1,
            digito_c0,digito_c1,
            digito_d0,digito_d1,
            digito_e0,digito_e1,
            digito_f0,digito_f1,
            digito_g0,digito_g1,
            digito_h1,digito_h1,
            digito_i0,digito_i1,
            digito_j0,digito_j1,
            digito_k0,digito_k1]

    saidas_1 = [-1,-1, #a
            -1,-1, #b
            -1,-1, #c
            -1,-1, #d
            -1,-1, #e
            -1,-1,
            -1,-1,
            -1,-1,
             1, 1, #i
             1, 1,
             1, 1]

    saidas_2 = [-1,-1,
            -1,-1,
            -1,-1,
            -1,-1,
             1, 1,
             1, 1,
             1, 1,
             1, 1,
            -1,-1,
            -1,-1,
            -1,-1]

    saidas_3 = [-1,-1,
            -1,-1,
             1, 1,
             1, 1,
            -1,-1,
            -1,-1,
             1, 1,
             1, 1,
            -1,-1,
            -1,-1,
             1, 1]

    saidas_4 = [-1,-1,
             1, 1,
            -1,-1,
             1, 1,
            -1,-1,
             1, 1,
            -1,-1,
             1, 1,
            -1,-1,
             1, 1,
            -1,-1]


    neuron_1 = Pydaline()
    neuron_2 = Pydaline()
    neuron_3 = Pydaline()
    neuron_4 = Pydaline()

    neuron_1.setEntradas(entradas)
    neuron_2.setEntradas(entradas)
    neuron_3.setEntradas(entradas)
    neuron_4.setEntradas(entradas)

    neuron_1.setSaidasDesejadas(saidas_1)
    neuron_2.setSaidasDesejadas(saidas_2)
    neuron_3.setSaidasDesejadas(saidas_3)
    neuron_4.setSaidasDesejadas(saidas_4)

    #neuron_1.setDebug(False)
    #neuron_2.setDebug(False)
    #neuron_3.setDebug(False)
    #neuron_4.setDebug(False)

    neuron_1.aprender()
    neuron_2.aprender()
    neuron_3.aprender()
    neuron_4.aprender()

    print "Épocas do neurônio 1:",neuron_1.epocas
    print "Épocas do neurônio 2:",neuron_2.epocas
    print "Épocas do neurônio 3:",neuron_3.epocas
    print "Épocas do neurônio 4:",neuron_4.epocas

if __name__ == "__main__":
    main()
