## VII Maratona de Programação InterIF – 2024

# Problema A - Joilson, o Anti-Social

**Autor**: Carlos José de Almeida Pereira (IFSP – São Carlos)  
**Arquivo**: `joilson.c | joilson.cpp | joilson.cs | joilson.java | joilson.py`  
**Tempo limite**: 1 segundo

## Descrição

Joilson adora ir ao cinema. Porém, ele tem uma característica anti-social: **não gosta de pessoas muito perto dele**. Ele acha que elas fazem barulho — conversando, comendo pipoca, se mexendo nas cadeiras, olhando o celular —, o que atrapalha sua concentração no filme.

Para evitar isso, Joilson sempre chega um pouco atrasado ao cinema, observa a disposição das pessoas e **escolhe o lugar com menos vizinhos ocupados**, sejam laterais, frontais, traseiros ou diagonais (até 8 vizinhos).

Por exemplo, considere a seguinte configuração da sala:

```
1 1 1  
0 0 1  
1 1 0  
1 0 1
```

- Cadeiras vazias: **4, 5, 9 e 11**.
- Vizinhos ocupados:
  - Cadeira 4 → 4 vizinhos
  - Cadeira 5 → 6 vizinhos
  - Cadeira 9 → 3 vizinhos
  - Cadeira 11 → 4 vizinhos

Joilson escolheria a **cadeira 9**, pois tem menos vizinhos ocupados.

## Entrada

A primeira linha contém dois inteiros `X` e `Y` (1 ≤ X ≤ 20, 2 ≤ Y ≤ 20), onde:
- `X` representa o número de **fileiras**,
- `Y` representa o número de **cadeiras por fileira**.

Em seguida, são fornecidas `X` linhas com `Y` valores cada, sendo:
- `1` para **ocupado**,
- `0` para **vazio**.

## Saída

A saída deve conter `Z + 1` linhas:

1. A primeira linha apresenta o **menor número de vizinhos ocupados** entre todas as cadeiras vazias.
2. As `Z` linhas seguintes contêm os **números das cadeiras** com essa menor quantidade de vizinhos, em ordem crescente.

A **numeração das cadeiras** começa em 1 e segue linha por linha da esquerda para a direita.

> Sempre haverá ao menos uma cadeira vazia.

---

## Exemplos

### Exemplo 1

**Entrada**
```
4 3
1 1 1
0 0 1
1 1 0
1 0 1
```

**Saída**
```
3
9
```

---

### Exemplo 2

**Entrada**
```
2 3
1 1 1
0 0 1
```

**Saída**
```
2
4
```

---

### Exemplo 3

**Entrada**
```
3 4
1 1 1 0
1 1 1 1
0 1 1 1
```

**Saída**
```
3
4
9
```

---

### Exemplo 4

**Entrada**
```
7 5
1 1 1 1 0
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
0 1 1 1 1
```

**Saída**
```
0
18
```