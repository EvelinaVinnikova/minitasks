def parse_matrix(input_string):
    rows = input_string.split('|')
    matrix = []
    for row in rows:
        float_row = [float(num) for num in row.strip().split()]
        matrix.append(float_row)
    return matrix

input_data = "1 2 | 3 4"
matrix = parse_matrix(input_data)
print(matrix)
assert matrix == [[1.0, 2.0], [3.0, 4.0]]
input_data1 = "12  4| -1 5  | 3 5 7 | 7 10 11111  "
matrix = parse_matrix(input_data1)
print(matrix)
assert matrix == [[12.0, 4.0], [-1.0, 5.0], [3.0, 5.0, 7.0], [7.0, 10.0, 11111.0]]
input_data2 = "10000  6| -1000 7.9"
matrix = parse_matrix(input_data2)
print(matrix)
assert matrix == [[10000.0, 6.0], [-1000.0, 7.9]]
input_data3 = "                  10.9999  4| -1 5 | 8686 | 6 5  4 7 433 57 "
matrix = parse_matrix(input_data3)
print(matrix)
assert matrix == [[10.9999, 4.0], [-1.0, 5.0], [8686.0], [6.0, 5.0, 4.0, 7.0, 433.0, 57.0]]

