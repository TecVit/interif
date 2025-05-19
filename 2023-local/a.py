def listar_primos_ate_n(N):
    if N < 2:
        return []

    # Cria uma lista booleana para a técnica da "Crivo de Eratóstenes"
    eh_primo = [True] * (N + 1)
    eh_primo[0] = eh_primo[1] = False  # 0 e 1 não são primos

    for i in range(2, int(N ** 0.5) + 1):
        if eh_primo[i]:
            for j in range(i * i, N + 1, i):
                eh_primo[j] = False

    primos = [i for i, primo in enumerate(eh_primo) if primo]
    return primos

# Entrada do usuário
N = int(input())

# Recuperando os primos perdidos
primos_encontrados = listar_primos_ate_n(N)

# Exibindo os resultados
print(" ".join(map(str, primos_encontrados)))
