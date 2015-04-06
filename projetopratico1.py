# encoding: utf-8
import os
import sys
import re
from pydaline import Pydaline

dataset = [[float(coluna) for coluna in linha.split(' ')] for linha in open('dados.txt').read().split('\n')[1:] if linha!='']
pesos_set = [[float(coluna) for coluna in linha.split(' ')] for linha in open('pesos.txt').read().split('\n') if linha!='']
dataset_questao3 = [[float(coluna) for coluna in linha.split(' ')] for linha in open('questao3.txt').read().split('\n') if linha!='']

entradas = [(linha[0], linha[1], linha[2]) for linha in dataset if len(linha)==4]
saidas_desejadas = [linha[3] for linha in dataset if len(linha)==4]

#plotagem
def plot():
    try:
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
    except ImportError:
        os.system('pip install matplotlib')
        plot()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    pureza_tipo1_x = [linha[0] for linha in dataset if int(linha[3]) == 0]
    pureza_tipo1_y = [linha[1] for linha in dataset if int(linha[3]) == 0]
    pureza_tipo1_z = [linha[2] for linha in dataset if int(linha[3]) == 0]

    pureza_tipo2_x = [linha[0] for linha in dataset if int(linha[3]) == 1]
    pureza_tipo2_y = [linha[1] for linha in dataset if int(linha[3]) == 1]
    pureza_tipo2_z = [linha[2] for linha in dataset if int(linha[3]) == 1]

    ax.scatter(pureza_tipo1_x, pureza_tipo1_y, pureza_tipo1_z, c='r', marker='o')
    ax.scatter(pureza_tipo2_x, pureza_tipo2_y, pureza_tipo2_z, c='r', marker='x')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

def exercicio_2():
    neuronio = Pydaline()
    for i, amostra in enumerate(dataset_questao3):
        print "\nAmostra %d"%(i+1)
        for treinamento in pesos_set:
            neuronio.pesos = treinamento 
            sys.stdout.write(str(neuronio.get_saida(dataset_questao3[i]))+" ")

def exercicio_1():
    neuronio = Pydaline()
    neuronio.set_entradas(entradas)
    neuronio.set_saidas_desejadas(saidas_desejadas)
    neuronio.set_debug(False)
    neuronio.aprender()

if __name__=='__main__':
    if len(sys.argv) == 1:
        print u"Opções:"
        print "python projetopratico1.py plot"
        print "python projetopratico1.py ex1"
        print "python projetopratico1.py ex2"
    elif 'plot' in sys.argv:
        plot()
    elif 'ex1' in sys.argv:
        exercicio_1()
    else:
        exercicio_2()
