def main():
    a = float(input())
    b = float(input())
    c = float(input())
    
    pontos = [a, b, c]
    equipe = ["A", "B", "C"]
    
    big = max(pontos)
    
    if pontos.count(big) > 1:
        print("Empatou")
    else:
        print(f"Equipe {equipe[pontos.index(big)]} Ganhou")
    
    return 0

if __name__ == "__main__":
    main()