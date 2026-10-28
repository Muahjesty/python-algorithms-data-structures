import math

def main():
    numbers = []
    
    # keep collecting nums using while loop
    while True:
        try:
            line = input()
            #if it matches str then break
            if line.strip() == "-12345":
                break
            numbers.append(int(line))
        except EOFError:
            break

    n = len(numbers)
    if n == 0:
        return

    # get mean
    mean_val = sum(numbers) / n
    
    # get median
    sorted_nums = sorted(numbers)
    if n % 2 != 0:
        # odd counts- take the middle using floor division index
        median_val = float(sorted_nums[n // 2])
    else:
        # even counts- average the two middle numbers
        mid1 = sorted_nums[(n // 2) - 1]
        mid2 = sorted_nums[n // 2]
        median_val = (mid1 + mid2) / 2.0

    # get sd (sigma)
    if n > 1:
        # use a list to get squared diffs
        squared_diffs = [(x - mean_val) ** 2 for x in numbers]
        # div the variance sum by (n - 1) and get the square root
        std_dev_val = math.sqrt(sum(squared_diffs) / (n - 1))
    else:
        std_dev_val = 0.0

    print(f"mean: {mean_val}")
    print(f"median: {median_val}")
    print(f"standard deviation: {std_dev_val}")

if __name__ == "__main__":
    main()
