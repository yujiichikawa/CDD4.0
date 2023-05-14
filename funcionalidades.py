import random

def verifPalavraRe(historicoLetra,letra):
    for p in historicoLetra:
        if p == letra:
            return True
    return False

def chutarPalavra(palavra):
    print("#### Palavra ####")
    tntpalavra = input()
    if palavra == tntpalavra:
        print("Parabéns, você ganhou!!!")
    else:
        print(f"Você perdeu!\nPalavra correta: {palavra}")

    return True

def geradorUnderline(palavra,historicoLetra):
    tabela = ""
    for j in palavra:
        achou = False
        for i in historicoLetra:
            if i == j:
                achou = True
                tabela += j

        if not achou:
            tabela += "_"
    return tabela

def tela(titulo,historicoLetra,qtdLetras):
    print(f"####### Tema: {titulo} #######")
    print(f"Quantidade de Letras: {qtdLetras}")
    print("_"*100)
    print(f"Tentativas: {' '.join(historicoLetra)}")
    print("_" * 100)
    print('____')
    print('|  0')
    print('|')
    print('|\n')

def palavraRandom(tempTema):
    palavra = ""
    num = random.randint(0, 5)
    for i in range(len(tempTema)):
        if i == num:
            palavra = tempTema[i].lower()

    return palavra

def gameplay(tema,titulo):
    end = False
    palavra = palavraRandom(tema)
    qtdLetras = len(palavra)
    historicoLetra = []
    while end == False:
        tela(titulo,historicoLetra,qtdLetras)

        tabela = geradorUnderline(palavra,historicoLetra)
        print(tabela)

        print("[1]- Digitar a Letra")
        print("[2]- Chutar a palavra")

        try:
            opt = int(input("Opção:"))
        except ValueError:
            print("Opção deve ser numérica")
            continue

        match opt:
            case 1:
                count = 0
                for i in tabela:
                    if i == "_":
                        count += 1
                if count == 1:
                    end = chutarPalavra(palavra)
                else:
                    print("#### Letra ####")
                    letra = input()
                    veri = verifPalavraRe(historicoLetra,letra)
                    if veri:
                        print("Palavra já citada")
                        continue

                    historicoLetra.append(letra)

            case 2:
                end = chutarPalavra(palavra)
            case _:
                pass

