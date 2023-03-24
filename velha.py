# Define o tabuleiro do jogo da velha
tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define as posições vencedoras
vencedores = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Define a função para imprimir o tabuleiro
def imprime_tabuleiro():
    print("|" + tabuleiro[0] + "|" + tabuleiro[1] + "|" + tabuleiro[2] + "|")
    print("|" + tabuleiro[3] + "|" + tabuleiro[4] + "|" + tabuleiro[5] + "|")
    print("|" + tabuleiro[6] + "|" + tabuleiro[7] + "|" + tabuleiro[8] + "|")

# Define a função para verificar se alguém ganhou
def verifica_ganhador():
    for jogador in ["X", "O"]:
        for a, b, c in vencedores:
            if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador:
                print(f"O jogador {jogador} venceu!")
                return True
    return False

# Define a função principal do jogo
def jogar_jogo():
    jogador = "X"
    jogadas = 0
    while True:
        imprime_tabuleiro()
        escolha = input("É a vez do jogador " + jogador + ". Escolha uma posição (de 1 a 9): ")
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha >= 1 and escolha <= 9:
                if tabuleiro[escolha - 1] == " ":
                    tabuleiro[escolha - 1] = jogador
                    jogadas += 1
                    if verifica_ganhador():
                        imprime_tabuleiro()
                        return
                    elif jogadas == 9:
                        print("Deu velha!")
                        imprime_tabuleiro()
                        return
                    jogador = "O" if jogador == "X" else "X"
                else:
                    print("Essa posição já foi escolhida. Tente outra.")
            else:
                print("Escolha uma posição válida (de 1 a 9).")
        else:
            print("Escolha uma posição válida (de 1 a 9).")

# Executa o jogo
jogar_jogo()
