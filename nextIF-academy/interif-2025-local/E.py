def main():
  n, m = map(int, input().split())

  pista = [[0] * (m + 2) for _ in range(n + 2)]

  for i in range(1, n + 1):
    linha = list(map(int, input().split()))

    for j in range(1, m + 1):
      pista[i][j] = linha[j - 1]

  start = (0, 0)
  sentido = 0
  perigo = 0
  fim = False

  # Sentidos
  # 0 -> Direita
  # 1 -> Baixo
  # 2 -> Esquerda
  # 3 -> Cima

  # (y, x)
  andar = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
  ]
  
  for i in range(1, n):
    indice = pista[i].index(1)
    
    if indice != -1:
      start = (i, indice)
      break

  fila = []
  fila.append(start)

  while len(fila) > 0:
    y, x = fila.pop(0)

    dy, dx = andar[sentido]

    if pista[y + dy][x + dx] == 2:
      perigo += 1

    tentativas = 0

    while pista[y + dy][x + dx] != 1:
      if tentativas > 1:
        fim = True
        break

      sentido += 1
      
      if sentido == 4:
        sentido = 0
        tentativas += 1

      dy, dx = andar[sentido]

    if fim:
      break

    fila.append((y + dy, x + dx))
    
    pista[y][x] = 0

  print(perigo)

  return 0

if __name__ == "__main__":
  main()