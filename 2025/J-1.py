def numero_e_primo(n):
  raiz = int(n ** (1 / 2)) + 1
  primo = True

  for i in range(2, raiz, 1):
    if n % i == 0:
      primo = False
      break

  return primo

def divisores_positivos(n):
  if n == 1:
    return 1
  
  qtd = 1

  for i in range(2, n + 1, 1):
    if n % i == 0:
      qtd += 1
  
  return qtd

def main():
  qtd = int(input())

  numeros = list(map(int, input().split()))
  numeros.sort(reverse=True)

  divisores = 0

  divisores_anterior = 0
  numero_escolhido = 0

  for numero in numeros:
    e_primo = numero_e_primo(numero)

    if e_primo:
      divisores = 2
    else:
      divisores = divisores_positivos(numero)
      
    if divisores_anterior == 0:
      divisores_anterior = divisores
      numero_escolhido = numero
    else:
      if divisores_anterior == divisores:
        if numero < numero_escolhido:
          numero_escolhido = numero
      else:
        break
  
  print(numero_escolhido)

  return 0

if __name__ == "__main__":
  main()