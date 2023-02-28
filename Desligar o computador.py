import os

print("Timer para desligar o computador")

print("1 - Desligar o computador em tempo X \n2 - Abortar o desligamento\n3 - Sair."  )

lang = input("O que deseja fazer? ")
match lang :
    case "1":
        qntdMinutos = int(input("Entre com o tempo necessário(minutos)"))
        tempoFinal = qntdMinutos*60
        str1 = "shutdown /s /t "
        str2 = str(tempoFinal)
        strFinal = str1 + str2

        os.system(strFinal)
        os.system(cls)
    case "2":
        os.system('shutdown -a')
    case "3":
        print("Você selecionou sair.")
