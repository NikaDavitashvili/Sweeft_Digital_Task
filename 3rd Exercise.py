def bomber_man(final_grid, n):
    if n > 3:
       n = 3
       print("\nAfter 3 seconds every result will be Same\nSo I will show you final result!")
    elif n <= 0: 
        n = 3
        print("\nError Occured, You have entered time\nIncorrectly So I will show you final result!")
    print("\nEnter Dimensions:")
    r = int(input("Row - "))
    c = int(input("Column - "))
    print(f"Your grid is [{r},{c}] and everything out of this borders will be IGNORED")
    print("\nPlant some bombs('O' or 'o' - Bomb, '.' - Clear)")
    final_grid = [list(input()) for _ in range(r)]
    bombs = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if final_grid[i][j] == 'o' or final_grid[i][j] == 'O' : bombs[i][j] = 2

    count = 1
    while count < n:
        count += 1
        if count%2 == 0:
            for i in range(r):
                for j in range(c):
                    if bombs[i][j] > 0:
                        bombs[i][j] -= 1
                    else:
                        bombs[i][j] = 3
        else:
            exploded = [[False]*c for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    bombs[i][j] -= 1
                    if bombs[i][j] == 0:
                        exploded[i][j] = True
                        if i > 0: exploded[i-1][j] = True
                        if j > 0: exploded[i][j-1] = True
                        if i < r-1: exploded[i+1][j] = True
                        if j < c-1: exploded[i][j+1] = True
            for i in range(r):
                for j in range(c):
                    if exploded[i][j]: bombs[i][j] = 0
                   
    for i in range(r):
        for j in range(c):
            final_grid[i][j] = 'O' if bombs[i][j] != 0 else '.'
    if n == 3:
        print(f"\nResults in or after {n}secs('O' - Safe, '.' - Exploded)")
        return '\n'.join(map(lambda res: ''.join(res), final_grid))
    elif n == 2:
        print(f"\nResults in {n}secs(Some bombs are Fake)")
        return '\n'.join(map(lambda res: ''.join(res), final_grid))
    elif n == 1:
        print(f"\nResults in {n}sec('.' - Safe, 'O' - Bomb)")
        return '\n'.join(map(lambda res: ''.join(res), final_grid))

print("\t\tBomberMan\n")
final_grid = []
n = int(input("Enter the second you want to check grid - "))
print(bomber_man(final_grid, n))
