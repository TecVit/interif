def main():
  n = int(input())
  l = [int(input()) for _ in range(n)]

  v = int(input())

  l.sort(reverse=True)

  i, c = 0, 0

  while v > 0:
    if v % l[i] == 0:
      c += v // l[i]
      v = 0
    elif v - l[i] >= 0:
      v -= l[i]
      c += 1
    else:
      if i + 1 >= n:
        break
      i += 1

  if v > 0:
    print(f"frustraka")
  else:
    print(c)

  return 0

if __name__ == "__main__":
  main()