"""
Arrays: São estruturas para manipulação de dados numericos em forma de vetores e matrizes

Numpy: É muito rapida e implementa diversas ferramentas para analisa de dados

import numpy as np

Possibilita trabalhar com estruturas n-dimenisonais 
array = (linha,coluna,profundidade)

axis -> É a direção ao longo dos dados
3d -> (x,y,z)

"""

import numpy as np
""" l = [1,2,3]
x = np.array(l)
print(x) #informa o meu array
print(type(x))
print(x.shape)#Informa a quantidade de array 
 """
#CASE EU QUISER COLOCAR ND=2 (2 DIMENÕES), BASTA APENAS COLOCAR DUAS LISTAS 
""" listas = [[1,2],[5,9]] #2 linhas e 2 colunas
x = np.array(listas)
print("z:\n", x)
print(x.shape) #MEUS NUMEROS DE ELEMENTOS NO ARRANJO, POR AXIS """
#Minha fucção reshape permite eu remodelar as minhas array, de acordo com a quantidade de elementos
# se eu tiver uma shape = (3,4) por fazer um reshape = (2,6)


#np.zeros -> quando queremos criar um array composto apenas por zero
"Ele não transforma a informação uma lista no array contidos por zeros "
""" print(np.zeros(shape=(2,2)))#Criando um array só com zeros
dim = (2,3) # 2 linhas e 3 colunas (shape(2,3))
x = np.zeros(dim) 
print("x:\n", x)
print(x.shape) """

#np.ones -> quando queremos criar um array composto por varios 1's
""" dim = (4,4)
x_one = np.ones(dim)
print("\n", x_one)
print(x_one.shape)
 """

#np.linspace
""" x_min,x_max = 10,50
x_total = np.linspace(x_min,x_max,num=10,dtype=None) #gera numeros aleatorios e com espaçamentos
x_second = np.linspace(x_min,x_max,num=5)
print(x_total)
print(x_second) """

#np.eye
#Coloca de forma aleatorio uma matriz com o shape que eu definir, com zeros e um's, não quer dizer que será sempre quadratica
# os um's ficaram sempre na diagonal
""" valor = np.eye(3,2)
valor_1 = np.eye(4)#Aqui será 4 linhas e 4 colunas
print(valor)
print(valor_1) """

#np.random.random
#Aqui vai fornecer no array, valores aleatorios entre 0 e 1, de acordo com o meu shape definido
""" value = np.random.random(size=(3,3))
print(value) """


#INDEXAÇÃO DE ARRAYS
# A TECNICA DE SLICE É OCORRE O COMPARTILHAMENTO DE MEMORIA
""" lista = [[2,6,7,11],[13,15,0,20],[21,45,12,80]]
test = np.array(lista)
print(test[1,1]) #AQUI ESTOU ACESSANDO UM ARRAY BIDIMENSIONAL TEST = (LINHA, COLUNA)
#NORMAMENTE REPRESENTADO POR (I,J)

print(test[-3]) #FATIANDO UM ARRAY BIDIMENSIONAL (linha, coluna) -> [-3:-1,1:3] -> [[6,7],[15,0]]
print(test[-3:-1,1:3]) # Sempre será B[i:k, j:l], k-1 e l-1 """

""" value = np.random.random(size=(3,4))
print(value)
central_value = value[1:3,1:3]
print(central_value)
 """


#OPERAÇÕES ARIMETRICAS 
"""
Operações de elemento a elemtento:
Soma: 
    np.add
Subtração:
    np.subtract
Dvisião:
    np.divide
Multiplicação
    Elemento a Elemento: np.multiply
    Matricial:
        Python puro: a@b 
        numpy:
            np.dot(a,b)
            a.dot(b)

Broadcasting: permite ganharmos despenho e poupar memorias

"""

""" a = np.array([[1,2],[3,8],[10,5]])
print(a)
b = np.array([2,9])

valor = np.dot(a,b)
valor_soma = np.add(a,3)#UMA IMPORTANTE OBSERVAÇÃO É O QUE É UM NUMERO INTEIRO (USAMOS BROADCASTING)
print(valor)
print(np.subtract(a,b))
print(valor_soma)
print(a*2) """

print("Hello World")



"""
Exemplo:
Sistema de equação

1*a + 2*b = 7
3*a - 2*b = -11
"""
""" matriz_a = np.array([[1,2],[3,-2]])
print(matriz_a.ravel())
matriz_c = np.array([[7],[-11]]) """
""" matrix_x = np.array([a],[b]) """
""" 
inv_matriz_a = np.linalg.inv(matriz_a)
result = np.dot(inv_matriz_a,matriz_c) # formula do sistema é matriz_a^-1 * matriz_c
print(result)
print(result.ravel()) #O ravel serve para deixar tudo na mesma linha 

x = np.dot(matriz_a,np.array([[2,2],[3,3]]))
print(x)
 """



#Comparações (extremamente utilizado)
"""
Comparações é a forma se um par de array:
    - maior ou menor:
        Usamos os mesmos 
"""
""" a = np.array([1,2,3,4])
b = np.array([0,1,3,1]) """

""" print(a>=b)
print(a<=3)
 """
#Podemos guardar as variaveis que são true nas comparações dos arrays
""" cond = b < 2
print(cond)
c = b[cond]#Aqui estamos separando os valores que ficaram positivos na comparação 
print(c)

 """

#Indexação Boleana
#Pode ser utilizada como um filtro
""" 
x = np.array([[5,2],[4,0]])
y = np.array([1,2])
z = x[0,:]
print(z)
z[1] = 10
print(z) """
""" print(x>y)
cond = x > y
print(x[cond]) """
""" cond = x % 2 == 0
filter = x[cond]
print(filter)
print(len(filter)) """

print(np.ones((2,2)))

print("test 1 2 3")





