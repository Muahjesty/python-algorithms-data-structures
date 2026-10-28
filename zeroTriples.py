def main():
    num_list = []
    
    # collect list until it ends
    while True:
        try:
            line = input()
            if line.strip() == "-12345":
                break
            num_list.append(int(line))
        except EOFError:
            break

    length = len(num_list)
    triples = []

    # nested loop to get values clearly
    # index+1 so no dupes
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if num_list[i] + num_list[j] + num_list[k] == 0:
                    # get the raw match combo as a list
                    match = [num_list[i], num_list[j], num_list[k]]
                    triples.append(match)


    if len(triples) == 1:
        print("1 triple found:")
    else:
        print(f"{len(triples)} triples found:")
        
    for triple in triples:
        print(f"{triple[0]}, {triple[1]}, {triple[2]}")

if __name__ == "__main__":
    main()
