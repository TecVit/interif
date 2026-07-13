def sobreSegmento(px, py, x1, y1, x2, y2):
  cross = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
  if cross != 0:
    return False
  
  return min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2)

def pontoDentroPoligono(ponto, vertices):
  x, y = ponto
  n = len(vertices)

  dentro = False

  for i in range(n):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % n]

    if sobreSegmento(x, y, x1, y1, x2, y2):
      return True 

    if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
      dentro = not dentro

  return dentro

def main():
  n = int(input())
  vertices = [tuple(map(int, input().split())) for _ in range(n)]
  
  x, y = map(int, input().split())
  dentro = pontoDentroPoligono((x, y), vertices)

  if dentro:
    print("DENTRO")
  else:
    print("FORA")

  return 0

if __name__ == "__main__":
  main()