#nested list
matrix = []
for i in range (3):
    matrix.append([])
    for j in range (5):
        matrix [i].append(j)
print(matrix)

#list comprehension
matrix = [[j for j in range(5)]for j in range(3)]
print(matrix)