import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def validacao():
    base_dir = os.path.dirname(__file__)
    caminho_csv = os.path.join(base_dir, "usuario_senha.csv")
    usuario_senha = pd.read_csv(caminho_csv, sep = ";")
    
    while True:
        tentativa_usuario = input("digite o usuário: ")
        if  tentativa_usuario not in usuario_senha["usuario"].values:
            print("usuário inválido")
        else:
            break
    senha_correta = usuario_senha.loc[usuario_senha["usuario"] == tentativa_usuario, "senha"].values[0]
    while True:
        tentativa_senha = input("digite a senha: ")
        if tentativa_senha != str(senha_correta):
            print("senha inválida")
        else:
            break
    return print("bem-vindo")
    
        
def mostrar_tabela():
    print("parte 1: mostrar elementos basicos da tabela")
    base_dir = os.path.dirname(__file__)

   
    caminho_csv = os.path.join(base_dir, "data.csv")

    dados = pd.read_csv(caminho_csv, sep = ";")
    print("Dados completos lidos do CSV:")
    print(dados)
    return dados


def mostrar_alguns_dados(dados):

    print("\ncolunas do csv:")
    print(dados.columns)

    print("\nnumero de linhas e colunas")
    print(dados.shape)


    notas = dados["nota"]
    print(f"notas: \n {notas}")


    idades = dados["idade"]
    print(f"\nidades dos alunos: \n{idades}")
    return notas, idades
#finalizada a parte de exposição

def estatistica(notas, idades):
    print('calculos acerca dos dados da tabela:\n')

    medianotas = notas.mean()
    mediaidades = idades.mean()

    maxnotas = notas.max()
    maxidades= idades.max()

    minnotas = notas.min()
    minidades = idades.min()

    print(f"respectivamente a média, numero maximo e numero minimo de notas foi {medianotas:.2f}, {maxnotas}, {minnotas}")

    print(f"respectivamente a média, numero maximo e numero minimo de idades foi {mediaidades}, {maxidades}, {minidades}")
    
#agora pegaremos o aluno de maior e menor nota
def maiores_e_menores(notas, dados):
    maiorindice = notas.idxmax()
    menorindice = notas.idxmin()

    maiornota = dados.loc[maiorindice, "nota"]
    menornota = dados.loc[menorindice, "nota"]

    alunomaiornota = dados.loc[maiorindice, "nome"]
    alunomenornota = dados.loc[menorindice, "nome"]
    print(f"alunos de maior e menor nota- {alunomaiornota}: {maiornota} e {alunomenornota}: {menornota}")
    return maiornota, menornota
#gráfico
def ranking(dados):
    ranking = dados.sort_values(by = "nota", ascending=False)
    print('ranking dos alunos por nota')
    print(ranking[["nome", "nota"]])

def grafico(notas, maiornota, menornota, dados):
    cores = []

    for nota in notas:
        if nota == maiornota:
            cores.append("green")
        elif nota == menornota:
            cores.append("red")
        else:
            cores.append("blue")

    plt.bar(dados["nome"], dados["nota"], color=cores)

    plt.title("notas dos alunos")
    plt.xlabel("aluno")
    plt.ylabel("nota do aluno")



    plt.show()

def main():
    dados = mostrar_tabela()
    notas, idades = mostrar_alguns_dados(dados)
    estatistica(notas, idades)
    maiornota, menornota = maiores_e_menores(notas, dados)
    ranking(dados)
    grafico(notas, maiornota, menornota, dados)

validacao()
decisao = input("deseja fazer a análise a respeito das notas?").lower()
if decisao.startswith("s"):
    main()
else:
    print("tudo bem")
    sys.exit(0)