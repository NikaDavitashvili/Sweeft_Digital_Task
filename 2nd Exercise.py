def bigger_Is_greater(ent):
    a, b= len(ent) - 2, len(ent) - 1
    while not (ent[a] < ent[a+1] or a < 0):
        a -= 1
    if a < 0:
        return "No Answer, There is not any greater combination!" 
    while not (ent[b] > ent[a]):
        b -= 1
    ent[a], ent[b] = ent[b], ent[a]
    ent[a+1:] = reversed(ent[a+1:])
    return f"Next greater word: {''.join(ent)}"

n = int(input("Enter number of Iterations - "))
for _ in range(n):
    entry = list(input("\nEntry - "))
    print(bigger_Is_greater(entry))
