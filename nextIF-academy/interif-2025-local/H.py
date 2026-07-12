import math

def distanciaEuclidiana(p1, p2):
  x1, y1 = p1
  x2, y2 = p2

  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
  l, c, x0, y0, d = map(int, input().split())

  h = int(input())

  for i in range(h):
    x1, y1 = map(int, input().split())

    distancia = distanciaEuclidiana((x0, y0), (x1, y1))

    if distancia <= d:
      print("Uma casinha no meio de todas")
      return 0

  print("Uma casinha no meio do nada")

  return 0

if __name__ == "__main__":
  main()