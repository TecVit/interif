def main():
  n = int(input())
  m = int(input())

  maior = 0
  vencedor = ""

  for _ in range(n):
    nome = str(input())

    for _ in range(m):
      salto = str(input())

      if len(salto.split()) > 1:
        continue
      else:
        salto = float(salto)

        if salto > maior:
          maior = salto
          vencedor = nome

  print(vencedor)
  print(f"{maior:.2f}")

  return 0

if __name__ == "__main__":
  main()