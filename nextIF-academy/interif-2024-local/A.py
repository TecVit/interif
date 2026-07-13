def main():
  x, y = map(int, input().split())
  sala = [[0] * (y + 2)]

  for _ in range(x):
    sala.append([0] + list(map(int, input().split())) + [0])
  
  sala.append([0] * (y + 2))

  ds = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    # (0, 0), lugar dele
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
  ]

  cords = []
  menor = float("inf")

  for i in range(1, x + 1):
    for j in range(1, y + 1):
      lugar = sala[i][j]

      if lugar == 0:
        vizinhos = sum([sala[i + dy][j + dx] for dy, dx in ds])
        cord = (i * y) - (y - j)
        
        if vizinhos == menor:
          cords.append(cord)
        elif vizinhos < menor:
          menor = vizinhos
          cords = [cord]
  
  print(menor)
  for cord in cords:
    print(cord)

  return 0

if __name__ == "__main__":
  main()