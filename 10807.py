matrix_size = input()
matrix = input().split(" ")
search = input()
count = 0

for i in range(len(matrix)):
    if matrix[i] == search:
        count += 1
        
print(count)