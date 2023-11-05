import numpy as np
#Função principal para obter os resultados do problema proposto no enunciado
def main():
    np.set_printoptions(precision=4,suppress=True)
    print("Algoritmo para decomposição LU de uma matriz A e resolução de um sistema Ax=d.")
    print("Para demonstração dos resultados do código, utiliza-se a matriz 'A' e o vetor 'd' do teste disponibilizado no final do enunciado.")
    funcao = int(input("Digite 1 para resolver somente o problema de decomposição LU ou digite 2 para resolver um sistema tridiagonal"))
    n=20
    #Cria as variáveis com os dados fornecidos pelo enunciado
    a=np.zeros(n)
    a[n-1]=(2*n-1)/(2*n)
    d=np.zeros(n)
    for i in range(0,n-1):
        a[i]=(2*(i+1)-1)/(4*(i+1))
        d[i]=np.cos((2*np.pi*(i+1)**2)/(n**2))
    c=1-a
    b=np.full(n,2)
    A=[a,b,c]   
    #Condicional para mostrar os resultados conforme deseja o usuário
    if funcao==1:
        L,U=decomposicaoLU(A)
        print("Vetor u:", U)
        print("Vetor l:", L)
        imprimir=int(input(print("Caso queira visualizar as matrizes L e U em forma de lista de listas digite 1, caso contrário digite 0 para dar sequência.")))
        #Condicional para imprimir as matrizes em formato array.
        if imprimir==1:
            print("Matriz U:", print_matrizU(U,c))
            print("Matriz L:", print_matrizL(L))
        #Condicional para continuar da decomposição para resolução de sistemas
        continua = int(input("Caso queira visualizar a solução do sistema Ax=d do teste, digite 1. Caso contrário digite 0 para encerrar o código"))
        if continua==1:
            print("As raízes do sistema são:")
            print("x:",solucao_sistema(A,d))
        else: 
            exit()
    elif funcao==2:
        print("As raízes do sistema são:")
        print("x:",solucao_sistema(A,d))
#'A' deve ser uma matriz com n colunas e 3 linhas, sendo a primeira linha 'a', a segunda 'b' e a terceira 'c'. Caso a matriz A não esteja no formato comentado, pode-se utilizar a função lista_de_listas_para_vetores adiciona em funções complementares 

#Primeira função, utilizada para realizar a decomposição LU de uma matriz A 
def decomposicaoLU(A): 
    a,b,c=A[0],A[1],A[2]
    U,L=np.zeros(len(A[0])),np.zeros(len(A[0])) #cria os vetores U e L vazios
    #Valores iniciais 
    U[0]=b[0]
    L[0]=1
    #Laço para encontrar L,U, assim como disponibilizado no enunciado
    for i in range(1,len(A[0])):
        L[i]=a[i]/U[i-1]
        U[i]=b[i]-L[i]*c[i-1]
    return L,U
#Segunda função, utilizada para resolver um sistema Ax=d.
def solucao_sistema(A,d):
    LU=decomposicaoLU(A)
    L,U=LU[0],LU[1]
    x,y=np.zeros(len(d)),np.zeros(len(d)) #cria os vetores x e y vazios
    y[0]=d[0]
    for i in range(1,len(d)):
        y[i]=d[i]-L[i]*y[i-1]
    x[len(d)-1]=y[len(d)-1]/U[len(d)-1]
    for i in range(len(d)-2,-1,-1):
        x[i]=(y[i]-A[2][i]*x[i+1])/U[i]
    return x

#Códigos complementares
#Função criada para transformar uma matriz A tridiagonal da forma de lista de listas (array) para vetores, conforme descrito no enunciado. 
def lista_de_listas_para_vetores(A):
    a,b,c=np.zeros(len(A[0])),np.zeros(len(A[0])),np.zeros(len(A[0])) #cria os vetores a, b e c vazios
    for i in range(0,len(A[0])): #atribui valores aos vetores
        if i==0:
            a[i]=0
        else:
            a[i]=A[i][i-1]
        b[i]=A[i][i]
        if i==len(A[0])-1:
            c[i]=0
        else:
            c[i] = A[i][i + 1]
    B=a,b,c
    return(B)
#Função para imprimir a Matriz U em forma de lista de listas (array)
def print_matrizU(u,c):
    U=np.zeros((len(u),len(u))) #cria a matriz U vazia
    for i in range(len(u)): #atribui valores para matriz U
        U[i][i]=u[i]
        if i != len(u)-1:
            U[i][i+1]=c[i]
    U_matrix=np.matrix(U)
    return U_matrix
#Função para imprimir a Matriz L em forma de lista de listas (array)
def print_matrizL(l):
    L=np.zeros((len(l),len(l))) #cria a matriz U vazia
    for i in range(len(l)): #atribui valores para matriz U
        L[i][i]=1
        if i != len(l)-1:
            L[i+1][i]=l[i+1]
    L_matrix=np.matrix(L)
    return L_matrix

main()
