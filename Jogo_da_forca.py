import random
def confere_se_ganhou(palavra,letras):
    for letra in palavra:
        if not letra in letras:
            return False
    return True



def jogo(palavra):
    tentativas = 6
    ganhou = False
    letras = set()
    while tentativas > 0 and ganhou == False:
        print("Palavra:", end=" ")
        for letra in palavra:
            if(letra in letras):
                print(letra,end=" ")
            else:
                print("_", end = " ")
        print("\n")
        print("Tentativas restantes:", tentativas)
        print("Letras tentadas:",end=" ")
        if len(letras) == 0:
            print("Nenhuma")
        else:
            ordem_alfabetica = letras
            ordem_alfabetica = sorted(ordem_alfabetica)
            i = 0
            for letra in ordem_alfabetica:
                i+=1
                if i == 1:
                    print(letra,end="")
                else:
                    print(",",letra,end="")
           
        print("")
        print("")
        while True:
            print("Digite uma letra:")
            a = input()
            if len(a) > 1 or a.isalpha() == False:
                print("Entrada inválida")
                continue
            else:
                letras.add(a.upper())
                break
        if a.upper() in palavra:
            print("Boa! A letra '{}' está na palavra.".format(a.upper()))
            if confere_se_ganhou(palavra,letras):
                ganhou = True
        else:
            print("A letra '{}' não está na palavra.".format(a.upper()))
            tentativas -= 1
        print("\n")
    
    if ganhou:
        print("Parabéns! Você acertou a palavra:", palavra)
    else:
        print("Fim de jogo! A palavra era:", palavra)


try:
    with open("palavras.txt", "r") as arquivo:
        numero = random.randint(0,19)
        palavras = arquivo.readlines()
        if len(palavras) == 0:
            print("arquivo vazio")
            exit()
        palavra = palavras[numero][0:-1]
        print("Bem-vindo ao Jogo da Forca!\n")
        jogo(palavra)
except FileNotFoundError:
    print("Arquivo não encontrado!")
    exit()
except IOError:
    print("ERRO ao abrir o arquivo")
    exit()




