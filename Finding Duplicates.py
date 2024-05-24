
a = "Sapna Kumari"

duplicates = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j] and a[i] not in duplicates:
            duplicates.append(a[i])


print("Duplicates:", duplicates)