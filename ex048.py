arriba = 0
for index in range(1, 501):
    if index % 2 == 1 and index % 3 == 0:
        arriba += index
print(arriba)
