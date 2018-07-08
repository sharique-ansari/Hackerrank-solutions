w1 = input()
w2 = input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total += len(w1) + len(w2) - 2 * len(set(w1.split()).intersection(set(w1.split())))
print(int(total/26))