def main():
  n, m = map(int, input().split())

  pista = [[0] * (m + 2) for _ in range(n + 2)]
  
  y, x = 0, 0
  achou_inicio = False

  for i in range(1, n + 1, 1):
    linha = list(map(int, input().split()))
    
    for j in range(1, m + 1, 1):
      if linha[j-1] == 1 and not achou_inicio:
        y, x = i, j
        achou_inicio = True

      pista[i][j] = linha[j-1]
  
  ds = {
    "top": (-1, 0),
    "right": (0, 1),
    "bottom": (1, 0),
    "left": (0, -1),
  }

  fila = [(y, x)]
  sentido = 'right'
  perigos = 0
  
  while len(fila) > 0:
    y, x = fila.pop()
    pista[y][x] = 0

    dy, dx = ds[sentido]

    if pista[y + dy][x + dx] == 1:
      fila.append((y + dy, x + dx))
    else:
      if pista[y + dy][x + dx] == 2:
        perigos += 1

      drs = ["top", "right", "bottom", "left"]
      
      for dr in drs:
        dy, dx = ds[dr]

        if pista[y + dy][x + dx] == 1:
          fila.append((y + dy, x + dx))
          sentido  = dr
          break
  
  print(perigos)

  return 0

if __name__ == "__main__":
  main()