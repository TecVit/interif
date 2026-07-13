MOD = 2**64

def fibonacci(n):
  dp = [0, 1, 1]

  while n > 0:
    dp.append(dp[-1] + dp[-2] + dp[-3])
    n -= 1
  
  return dp

def main():
  n = int(input())

  lista = fibonacci(n - 1)
  resultado = lista[n + 1]

  print(resultado % MOD)

  return 0

if __name__ == "__main__":
  main()