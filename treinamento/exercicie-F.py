# Problema F
# Jogando Bocha

def main():
    d1= float(input())
    d2= float(input())
    d3= float(input())

    if d1 > d3 and d1 > d2:
        print("Equipe A ganhou")
    elif d2 > d3 and d2 > d1:
        print("Equipe B ganhou")
    elif d3 > d2 and d3 > d1:
        print("Equipe C ganhou")
    elif d1 == d2 and d2 == d3:
        print("Empatou")

    elif d1 == d2 and d3 > d1:
        print("Equipe C ganhou")
    elif d1 == d3 and d2 > d1:
        print("Equipe B ganhou")
    elif d2 == d3 and d1 > d3:
        print("Equipe A ganhou")
        
    elif d1 == d2 and d3 < d1:
        print("Empatou")
    elif d1 == d3 and d2 < d3:
        print("Empatou")
    elif d2 == d3 and d1 < d2:
        print("Empatou")

    return 0

if __name__ == "__main__":
    main()