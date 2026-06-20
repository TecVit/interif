def main():
  sequencia = input()
  
  anterior = sequencia[0]
  maior = 1
  contador = 1

  for i in range(1, len(sequencia)):
    atual = sequencia[i]

    if atual != anterior:
      anterior = atual
      contador += 1
    else:
      if contador > maior:
        maior = contador

  if contador > maior:
    print(contador)
  else:
    print(maior)

  return 0

if __name__ == "__main__":
  main()