def main():
  fila_normal = []
  fila_prioridade = []

  while True:
    entrada = input().split()

    # CHEGADA
    if len(entrada) > 1:
      nome, idade = entrada[1], int(entrada[2])
      
      if idade > 54:
        fila_prioridade.append((nome, idade))
      else:
        fila_normal.append((nome, idade))
    
    # ATENDIMENTO
    else:
      if len(fila_prioridade) > 0:
        nome, idade = fila_prioridade.pop(0)
      else:
        nome, idade = fila_normal.pop(0)
      
      print(nome)

if __name__ == "__main__":
  try:
    main()
  except:
    pass