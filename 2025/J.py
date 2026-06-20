def divisores_positivos(n):
  qtd = 0

  for i in range(1, n + 1, 1):
    if n % i == 0:
      qtd += 1
  
  return qtd

def main():
  qtd = int(input())
  numeros = list(map(int, input().split()))

  maior = 0
  escolhido = 0

  for numero in numeros:
    divisores = divisores_positivos(numero)

    if divisores > maior:
      maior = divisores
      escolhido = numero 
    elif divisores == maior:
      if numero < escolhido:
        escolhido = numero
  
  print(escolhido)

  return 0

if __name__ == "__main__":
  main()