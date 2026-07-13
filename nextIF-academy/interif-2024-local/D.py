def primosAteN(n):
  primos = []

  if n <= 1:
    return primos
  
  for i in range(2, n + 1):
    primo = True

    for j in range(2, i):
      if i % j == 0:
        primo = False
        break

    if primo:
      primos.append(i)

  return primos

def maiorNumeroDaLista(lista):
  maior = float("-inf")

  for numero in lista:
    if numero > maior:
      maior = numero

  return maior

def main():
  a, b = map(int, input().split())
  
  if a > b:
    n = a
  else:
    n = b

  primos = primosAteN(n)
  maior = maiorNumeroDaLista(primos)

  print(maior)
   
  return 0

if __name__ == "__main__":
  main()