def is_fibonacci(n):
    # Inicio da sequencia 
    a, b = 0, 1
    
    # Se o número informado for 0 ou 1, já sabemos que pertence à sequência
    if n == 0 or n == 1:
        return True
    
    # Faz o calculo da sequencia até superar o número informado. 
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    
    return False

while True:
    # Solicita o número ao usuário
    try:
        numero = int(input("Informe um número: "))

        # Verifica se o número pertence à sequência de Fibonacci
        if is_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Insira um número inteiro válido.")
    
    # Pergunta ao usuário se deseja continuar ou encerrar
    continuar = input("Deseja continuar a verificação? (sim/não): ").strip().lower()
    if continuar != 'sim':
        print("Encerrando o programa. Até logo!")
        break


