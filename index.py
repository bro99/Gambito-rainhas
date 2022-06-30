#Referencias matematicas https://www.youtube.com/watch?v=GJ6MftyWFHY&ab_channel=MestreCapivara
from itertools import permutations
import time
time_start = time.time()

def Contador():
    #Verificação para confirmar que se tratam de numeros inteiros - positivos e diferentes de 0
    while True:
        print("Escolha o tamanho do tabuleiro \n"  
                                "1 - 4x4\n"
                                "2 - 8x8\n"
                                "3 - 15x15\n"
                                "4 - 30x30\n"
                                "5 - 50x50\n"
                                "6 - 100x100\n"
                                "7 - 250x250\n"
                                "8 - 500x500\n"
                                "9 - 1000x1000\n")
        valorEscolhido = int(input())

        if valorEscolhido > 0 and valorEscolhido < 9:
            break


    # Uma lista para mostrar qual deve ser o valor real escolhido pelo user
    valorTabela = ['0,','4','8','15','30','50','100','250','500','1000']
    valorEscolhido = int(valorTabela[valorEscolhido])
    #passo o valor da escolha como indice para a nova variavel

    #Agora começa o calculo
    #COmo tenho possibilidades n X n - preciso criar uma matriz de [(n x n), [(n x n)]
    data = range(valorEscolhido)
    print(data)




    #Crio um contador que vai atribuir para novo indice um valor diferente para cada linha que ele passar
    #Pense em uma equação de X - Y | o que faz a atribuição para cada linha passada é ele!
    print("Um tabuleiro 8x8 possui 64 posições, ou seja para a primeira rainha 64 possibilidades.\n"
          "Para a segunda, temos 63 assim por diante\n"
          "Fatorial 8!\n"
          "(64!)/((64-8)x8!)\n"
          "Existem 92 possibilidades de soluções - desde espelhamento - rotações 90º - 180º\n")

    print("Valores em 0 são vistos como 8")
    input("Tecle Enter para continuar - >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    for board_X in permutations(data):
        Equal_X = set(
            board_X[i] + i
                      for i in data
        )
        newEqual_x = len(Equal_X)

        Equal_Y = set(
            board_X[i] + i
                      for i in data
        )
        newEqual_y = len(Equal_Y)

        # agora vem a escolha que muda o jogo rsrs.
        # Usando uma regra de agrupamento e permutações.
        if valorEscolhido == newEqual_y and newEqual_x:
            print(board_X)

if __name__ == '__main__':
    Contador()

print("--- %s segundos ---" % (time.time() - time_start))