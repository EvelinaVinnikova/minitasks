def parse_matrix(input_string):
    rows = input_string.split('|')
    matrix = []
    for row in rows:
        float_row = [float(num) for num in row.strip().split() if num]
        matrix.append(float_row)

    return matrix

input_data = "1 2 | 3 4"
matrix = parse_matrix(input_data)
print(matrix)
print(matrix[0][1])
