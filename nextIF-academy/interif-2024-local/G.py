def main():
  tabuleiro = str(input())

  for peca in tabuleiro:
    try:
      peca = int(peca)
      print("| " * peca, end="")
    except:
      if peca == "/":
        print("|")
      else:
        print(f"|{peca}", end="")
  
  print("|")

  return 0

if __name__ == "__main__":
  main()