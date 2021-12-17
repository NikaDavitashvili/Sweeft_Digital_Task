n = int(input("Enter amount of Words to Enter - "))
dict = {}
lst = []

for _ in range(n):
  entry = input()
  lst.append(entry)
  if entry in dict:
    dict[entry] += 1
  else:
    dict[entry] = 1
    
print(f"\nNumber of Distinct Words - {len(dict)}")
print(f"Every Word Occurance according to their appearance - ({', '.join([str(dict[ent]) for ent in dict])})\n")
