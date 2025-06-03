# Tempo de Conclusão: 19:39.32

def main():
    fila_normal = list()
    fila_prioridade = list() # (Nome, Idade)

    fim = False
    while fim == False or len(fila_normal) > 0:
        dados = list(map(str, input().split()))

        if dados[0] == "CHEGADA":
            nome = dados[1]
            idade = int(dados[2])

            if idade > 54:
                fila_prioridade.insert(0, (nome, idade))
            else:
                fila_normal.insert(0, (nome, idade))

        elif dados[0] == "ATENDIMENTO":
            if len(fila_prioridade) > 0:
                print(fila_prioridade[len(fila_prioridade) - 1][0])
                fila_prioridade.pop()
            elif len(fila_normal) > 0:
                print(fila_normal[len(fila_normal) - 1][0])
                fila_normal.pop()
            
            if len(fila_normal) == 0 and len(fila_prioridade) == 0:
                fim = True

    return 0

if __name__ == "__main__":
    main()