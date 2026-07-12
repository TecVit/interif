def main():
  sequencia = str(input())
  tamanho = len(sequencia)
  
  maior = 0
  contador = 1

  for i in range(tamanho - 1):
    letra = sequencia[i]
    prox_letra = sequencia[i+1]

    if prox_letra == letra:
      if contador > maior:
        maior = contador
      contador = 1
    else:
      contador += 1
  
  print(max(maior, contador))
    
  return 0

if __name__ == "__main__":
  main()