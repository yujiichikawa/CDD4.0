from funcionalidades import *

alimentos = ("Ratatouille","Lámen","Moussaka","Tacacá","Tacos","Poutine")
carros = ("BMW","Ford","Honda","Hyundai","Mitsubishi","Porsche")
paises = ("Australia","Albania","Argelia","Herzegovina","Bulgaria","Chipre")
times = ("Barcelona","Liverpool","Benfica","Chelsea","Juventus","Arsenal")

while True:
    print("########### G-A-M-E #################")
    print("[1]- Jogar")
    print("[0]- Sair")
    print("#####################################")
    try:
        opt = int(input("Opção:"))
    except ValueError:
        print("Opção deve ser numérica")
        continue

    match opt:
        case 1:
            while True:
                print("[1]- Escolher Tema")
                print("[2]- Aleatório")
                print("[0]- Voltar")

                try:
                    opt = int(input("Opção:"))
                except ValueError:
                    print("Opção deve ser numérica")
                    continue

                match opt:
                    case 1:
                        while True:
                            print("###### Temas ######")
                            print("[1]- Alimento")
                            print("[2]- Carro")
                            print("[3]- País")
                            print("[4]- Time")
                            print("[0]- Voltar")

                            try:
                                opt = int(input("Opção:"))
                            except ValueError:
                                print("Opção deve ser numérica")
                                continue

                            match opt:
                                case 1:
                                    gameplay(alimentos,"Alimento")
                                case 2:
                                    gameplay(carros,"Carro")
                                case 3:
                                    gameplay(paises,"Paises")
                                case 4:
                                    gameplay(times,"Time")
                                case 0:
                                    break
                                case _:
                                    pass
                    case 2:
                        num = random.randint(1,4)
                        if num == 1:
                            gameplay(alimentos,"Alimento")
                        elif num == 2:
                            gameplay(carros,"Carro")
                        elif num == 3:
                            gameplay(paises,"Paises")
                        elif num == 4:
                            gameplay(times,"Time")

                    case 0:
                        break

        case 0:
            break
        case _:
            pass
