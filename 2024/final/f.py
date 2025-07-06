def main():
    l = int(input())
    m = int(input())
    a = int(input())
    v = int(input())

    if v > l:
        print(m + ((v - l) * a))
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()