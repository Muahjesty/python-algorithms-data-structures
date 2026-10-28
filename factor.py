def main():
    try:
        line = input()
        if not line.strip():
            return
        n = int(line)
    except EOFError:
        return
    
    divisor = 2
    # loop until n is 1
    while n > 1:
        # check if div by n
        if n % divisor == 0:
            print(divisor, end=" ")
            # reducing n
            n //= divisor
        else:
            # incrementing
            divisor += 1
    print()  

if __name__ == "__main__":
    main()
