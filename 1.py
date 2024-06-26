z = input().split()
max_len = len(max(z, key=len))
for word in z:
    print(word.rjust(max_len, "*"))


