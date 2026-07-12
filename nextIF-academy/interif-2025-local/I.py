def main():
  alfabeto = "abcdefghijklmnopqrstuvwxyz"

  n, palavra, chave = map(str, input().split())
  n = int(n)

  tamanho = len(palavra)

  if n == 1:
    horario = True
  elif n == 2:
    horario = False
  
  nova_palavra = ""

  for i in range(tamanho):
    if horario:
      indice_palavra = alfabeto.index(palavra[i])
      indice_chave = alfabeto.index(chave[i])
      diferencia = indice_palavra - indice_chave - 1
      
      if diferencia < 0:
        diferencia += 26

      nova_palavra += alfabeto[diferencia]
      
      horario = False    
    else:
      indice_palavra = alfabeto.index(palavra[i])
      indice_chave = alfabeto.index(chave[i])

      diferencia = indice_palavra + indice_chave + 1
      if diferencia > 25:
        diferencia -= 26

      nova_palavra += alfabeto[diferencia]

      horario = True

    # print(indice_palavra)
    # print(indice_chave)
    # print("letra: ", alfabeto[diferencia])
    
  print(nova_palavra)

  return 0

if __name__ == "__main__":
  while True:
    try:
      main()
    except:
      break