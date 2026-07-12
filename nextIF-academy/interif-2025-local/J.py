def primosAteN(n):
  if n < 2:
    return []
  
  eh_primo = [True] * (n + 1)
  eh_primo[0] = eh_primo[1] = False

  for i in range(2, int(n ** 0.5) + 1):
    if eh_primo[i]:
      for j in range(i * i, n + 1, i):
        eh_primo[j] = False
  
  return {i for i in range(2, n + 1) if eh_primo[i]}

def totalDeDivisores(x):
  qtd = 2

  for i in range(x - 1, 1, -1):
    if x % i == 0:
      qtd += 1
  
  return qtd

def main():
  n = int(input())
  l = list(map(int, input().split()))
  
  primos = primosAteN(max(l))

  maior = 0
  numero = 0

  for x in l:
    if x in primos:
      divisores = 2
    else:
      divisores = totalDeDivisores(x)

    if divisores == maior:
      numero = min(numero, x)
    elif divisores > maior:
      maior = divisores
      numero = x
  
  print(numero)

  return 0

if __name__ == "__main__":
  main()