def main():
    n, m = map(int, input().split())
    friends = {}

    for _ in range(m):
        i, j = map(int, input().split())
        
        if i not in friends:
            friends[i] = [j]
        else:
            if j not in friends[i]:
                friends[i].append(j)
        
        if j not in friends:
            friends[j] = [i]
        else:
            if i not in friends[j]:
                friends[j].append(i)
    
    x = []
    c = 0

    for person in friends.keys():
        qtd = len(friends[person])

        # (Qtd amigos, Pessoa, Amigos)
        x.append((qtd, person, friends[person]))
    
    x.sort(reverse=True)
    visitado = set()

    for i in range(len(x)):
        qtd, person, friends_person = x[i]

        if person in visitado:
            continue

        visitado.add(person)

        for friend in friends_person:
            visitado.add(friend)
        
        c += 1

    print(c)

    return 0

if __name__ == "__main__":
    main()