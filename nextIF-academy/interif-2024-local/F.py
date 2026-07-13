def main():
  equipes = {
    "A": float(input()),
    "B": float(input()),
    "C": float(input()),
  }

  maior = 0
  empate = -1
  vencedor = ""

  for key in equipes.keys():
    if equipes[key] == maior:
      empate = maior
    if equipes[key] > maior:
      maior = equipes[key]
      vencedor = key

  if empate == maior:
    print("Empatou")
  else:
    print(f"Equipe {vencedor} ganhou")

  return 0

if __name__ == "__main__":
  main()