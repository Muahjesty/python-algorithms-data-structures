def is_increasing(num):
    # covert int into str to see digs in order
    digit_str = str(num)
    
    # loop thru digs upto second to last order
    for i in range(len(digit_str) - 1):
        if digit_str[i] >= digit_str[i + 1]:
            return False
    return True

def main():
    try:
        line = input()
        if not line.strip():
            return
        n = int(line)
    except EOFError:
        return

    increasing_count = 0
    
    # loop, range from 1 to n
    for number in range(1, n + 1):
        if is_increasing(number):
            increasing_count += 1
            
    print(increasing_count)

if __name__ == "__main__":
    main()