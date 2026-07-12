def limparFrase(frase: str):
  caracteres = [".", ",", ";", ":", "'", '''"''', "!", "?"]

  for caracter in caracteres:
    frase = frase.replace(caracter, "")
  
  return frase.lower()

def main():
  historico = {}

  while True:
    try:
      frase = limparFrase(str(input()))
    except:
      break

    palavras = frase.split()

    for palavra in palavras:
      if palavra in historico:
        historico[palavra] += 1
      else:
        historico[palavra] = 1
  
  lista_historico = [(key, historico[key]) for key in historico.keys()]

  lista_historico.sort(key=lambda x: (-x[1], x[0]))

  last_value = -1

  for key, value in lista_historico:
    if last_value != value:
      if last_value != -1:
        print()
      print(f"{value}: {key}", end="")
      last_value = value
    else:
      print(f" {key}", end="")

  return 0

if __name__ == "__main__":
  main()