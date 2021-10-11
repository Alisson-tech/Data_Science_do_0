#!/usr/bin/env python
# coding: utf-8

# ## Matrizes - 60
# 
# Matriz é uma coleção bidimensional de números, no python utilizaremos listas de listas.

# In[49]:


from typing import List, Tuple, Callable
import math


# In[ ]:


matrix = List[List[float]]


# In[ ]:


matriz = [[1,2,3],[5,6,7]] # 3 colunas, 2 linhas


# In[50]:


def shape(A: matrix) -> Tuple[int, int]: # Retorna o tamanho da matriz
    linhas = len(A)
    colunas = len(A[0])
    return linhas, colunas

shape(matriz)


# In[51]:


# Retornar todos elementos da linha i
def get_row(A: matrix, i: int) -> List[float]: 
    return A[i]



# In[52]:


#Retorna todos elementos dacoluna j
def get_column(A: matrix, j: int) -> List[float]: 
    return[a_i[j] for a_i in A]



# In[53]:


# Cria uma matriz
def criar_matriz(colunas : int,
                 linhas: int,
                 #Objeto do tipo função com lista de lista (i, j)
                 valores: Callable[[int,int], float]
                ) -> matrix:
    return[[valores(i,j) for j in range(colunas)] 
           for i in range(linhas)] #percorre i e j e gera lista de lista



# In[54]:


# Matriz identidade (NxN com 1 na diagonal principal
def matriz_identidade(n : int) -> matrix: 
    return criar_matriz(n,n, lambda i,j: 1 if i==j else 0)



# ## Redes de amigos - pg 62
# 
# Matriz de rede amigos
# (one-hot-encoding)

# In[55]:


#usuario      0, 1, 2, 3, 4, 5, 6, 7, 8, 9  
matriz_amigos = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # usuario 0
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # 1
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # 2
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # 3
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 4
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # 5
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # 6
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # 7
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # 8
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # 9



# In[57]:


amigos_cinco = [ i for i, amigos in enumerate(matriz_amigos[5]) 
               if amigos] # Enumere as colunas da linha 5
                          # Atribua o valor de i se amigo == 1  
amigos_cinco


# # Algebra Linear - Capitulo 4
# 
# ## Calculo de vetores - pg 56
# 
# - Soma (v_i + w_i)
# - Subtração(v_i - w_i)
# 
# 
# Soma ou Subtração de item por item de um vetor

# In[58]:


Vector = List[float]
def somar(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w) # Verificar se tamnhos iguais nas listas
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def subtrair(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v,w)]




# ## Calculos de vetores - pg 57
# 
# - soma de elementos
# - multiplicação escalar
# - média
# 
# ### Soma de elementos
# 
# Soma os elementos das lista pela posição. (lista dentro de lista)
# 
# ### Multiplicação escalar
# 
# Multiplica cada elemento da lista por um valor escolhido
# 
# ### Média
# 
# Utilizando as Funções a cima, tem como objetivo retornar uma lista de medias.
# 
# ela soma item por item da lista de acordo com sua posição e multiplica por 1/n, onde n é o comprimento da lista.
# 
# exemplo:
# 
# Uma professora quer ver as médias dos alunos ela passa uma lista com as notas da primeira e segunda prova, o programa retorna a média de cada aluno.
# 
# ((notas 1),(notas 2))
# 
# cada posição representa um aluno tanto para notas 1 quanto para notas 2, o programa retorna uma lista com a média de cada aluno de acordo com sua posição.

# In[59]:


def soma_elements(vectors:Vector) -> Vector:
    assert vectors
    num_elements = len(vectors[0]) # Lista dentro de lista
    assert all(len(v) == num_elements for v in vectors) #Verifica se as listas dentro da variavel tem mesmo tamanho
    
    return [sum(vector[i] for vector in vectors) 
           for i in range(num_elements)]



# In[60]:


def multplicacao_escalar(s:float, vectors:List[float]):
    return [s * v_i for v_i in vectors]



# In[61]:


def media(vectors:List[float]):
    n = len(vectors)
    return multplicacao_escalar(1/n, soma_elements(vectors))


# ## Calculos de vetores - pg 58
# 
# - Produto Escalar
# - Soma dos quadrados
# - Magnitude
# - Distância
# 
# ### Produto escalar
# 
# Função para Somar duas Multiplicações
# 
# ### Soma dos quadrados
# 
# somar cada item elevado ao quadrado, utilizando a função produto escalar para reliazar a potenciação.
# 
# 
# ### magnitude 
# 
# Basicamente Teoremas de pitagoras sendo funcional com a ajuda das duas funções descritas a cima.
# Usado para medir o comprimento entre os pontos.
# 
# ### Distancia
# 
# Mostra a distância entre vetores (pontos), ultilizando da função subtrair para obter a diferença entre os pontos e depois a função magnitude para realizar o Teorema de Pitagorás e obter a distancia entre os pontos.

# In[62]:


def produto_escalar (v: List[float], w: List[float]) -> float: #soma do resultado de uma multiplicação
    assert len(v) == len(w) # Verificar se tamnhos iguais nas listas
    
    return sum(v_i * w_i for v_i, w_i in zip(v,w))



# In[63]:


def soma_quadrados(v:List[float]) -> float:
    return produto_escalar(v,v)

assert soma_quadrados([1,2,3]) == 14


# In[64]:




# In[65]:


def magnitude(v:List[float]) -> float: #Representa o comprimento de um vetor (teorema de pitagoras)
    return math.sqrt(soma_quadrados(v))

    


# In[66]:


def distancia(v: List[float], w: List[float]) -> float: # Distancia entre dois vetores (v_i - w_i)**2
    return magnitude(subtrair(v , w))



# In[ ]:




