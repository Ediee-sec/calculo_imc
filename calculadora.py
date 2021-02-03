while True:
    peso = float(input("Infome o seu peso: "))
    altura = float(input("Infome a sua altura: "))
    imc = peso / (altura ** 2)
    print("O seu imc é " "%.1f" % imc)

    if imc < 18.5:
        print("Magreza")
    elif imc > 18.5 and imc < 24.9:
        print("Normal")
    elif imc > 24.9 and imc < 30:
        print("Sobrepeso")
    elif imc > 30:
        print("Obesidade")

    repetir = input("\nDeseja fazer novamente o calculo?(s/n): \n")
    if repetir == "s":
        continue
    else:
        break
