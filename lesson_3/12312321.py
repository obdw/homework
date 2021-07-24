i = 0
while i < 10:
    if i == 3:
        i += 2
        continue

    print(i)
    if i == 9:
        break

    i += 1