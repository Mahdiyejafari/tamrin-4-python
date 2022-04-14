from re import M


M = int(input())
h = int(input())

for row in range(1, M+1):
    print()
    for col in range(1, h+1):
        print(col * row, end="\t")