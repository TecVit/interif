def main():
    l, c, x0, y0, d = map(int, input().split())
    h = int(input())
    
    for i in range(h):
        x1, y1 = map(int, input().split())
        ds = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** (1 / 2)
        
        if ds <= d:
            print(f"Uma casinha no meio de todas")
            return 0

    print(f"Uma casinha no meio do nada")

    return 0

if __name__ == "__main__":
    main()