import re, time

def imc(peso, altura):
    altura = altura / 100
    r = peso / (altura**2)
    return round(abs(r), 1)

def menu():
    while True:
        try:
            opcao = int(input("Quer fazer uma nova operação? (1 - Sim, 2 - Não): "))
            if opcao not in [1,2]:
                raise ValueError("Opção inválida. Digite 1 para Sim ou 2 para Não.\n")
            else:
                return opcao
        except ValueError:
            print("Opção inválida. Digite 1 para Sim ou 2 para Não.\n")
            continue

def descrever():
    texto = """
Este modelo é um aplicativo Python que calcula o Índice de massa Corporal (IMC) de uma pessoa com base em seu peso e altura especificados pelo usuário.

Ao iniciar o programa o usuário é solicitado a inserir seu peso e altura. Em seguida, verifica se a entrada está correta, por exemplo, é um número positivo ou um decimal. Se a entrada for inválida, o programa exibirá uma mensagem de erro e solicitará que o usuário digite novamente o valor.

Depois de receber o item correto, o programa calculará o IMC usando fórmulas matemáticas relevantes. Em seguida, exibe o resultado do calculo para o usuário e informa o valor do IMC com duas casas decimais.

Depois disso, o programa perguntará ao usuário se deseja realizar uma nova ação ou cerrar o aplicativo. Ocorrência o usuário opte por continuar, o programa reinicia o processo de calculo do IMC. Ocorrência contrário, o programa fechará e exibirá uma mensagem de fim de processo.

O modelo usa a biblioteca re para verificar os registros de peso e altura. e exibe uma mensagem de erro para o usuário se o registro for inválido. O modelo também usa a função de arredondamento para arredondar o valor do IMC para uma casa decimal para apresentá-lo de forma mais clara ao usuário."""
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.01)

def acao():
    while True:
        try:
            while True:
                peso = input("Digite o Peso (Kg): ")
                if not re.match(r"^[0-9.]+$", peso):
                    print("Peso inválido: só números inteiros com ponto decimal")
                else:
                    peso = float(peso)
                    if peso < 0:
                        raise ValueError("O peso deve ser não negativo.")
                    break 
            
            while True:
                      
                altura = input("Digite a Altura (cm): ")
                if not re.match(r"^[0-9.]+$", altura):
                    print("Altura inválida: só números inteiros com ponto decimal")
                else:
                    altura = int(altura)
                    if altura < 0:
                        raise ValueError("A altura deve ser não negativa.")
                    break
            
        
            resultado = imc(peso, altura)

            print(f"\nSeu IMC é:  {resultado:.2f}\n>>>>>>>")
            
            action = menu()
            
            if action == 1:
                print("")
            
            if action == 2:
                print("\n==========\nFim de operação.\n")
                descrever()
                
                break
            
        except ValueError as erro:
            print(f"Valor inválido: {erro}. Por favor, tente novamente.")
            continue    
                
acao()
