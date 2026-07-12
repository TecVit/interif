def custos(n):
  dp = [0] * (n + 1)

  dp[1] = 2
  dp[2] = 3

  for k in range(3, n + 1):
    melhor = float("inf")

    for i in range(1, k):
      melhor = min(melhor, dp[i] * dp[k - i])

    dp[k] = melhor

  return dp[n]

def main():
  n = int(input())
  
  print(custos(n))

if __name__ == "__main__":
  main()