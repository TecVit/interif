def main():
    n = int(input())

    alfabeto = [
        'a', 'b', 'c', 'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
    ]
    
    for _ in range(n):
        name = str(input())
        response = ''

        # Subtrair 97 do número = i
        # alfabeto[i] = letra correta

        number = ''

        for letter in name:
            try:
                num = int(letter)
                total = int(str(number + letter))
                if total >= 97 and total <= 122:
                    i = total - 97
                    response = response + alfabeto[i]
                    number = ''
                else:
                    number = number + letter

            except:
                response = response + letter       

        print(response)

    return 0

if __name__ == "__main__":
    main()