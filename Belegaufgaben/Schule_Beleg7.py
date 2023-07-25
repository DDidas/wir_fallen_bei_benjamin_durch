import numpy as np

# Parsing the matrix from the LaTeX format
def parse_latex_matrix(input_str):
    rows = input_str.split("\\cr")[:-1]
    matrix = []
    for row in rows:
        row = row.strip()
        values = row.split("&")
        parsed_values = []
        for val in values:
            if val == 'x':
                parsed_values.append(val)
            else:
                parsed_values.append(float(val))
        matrix.append(parsed_values)
    return matrix

# Parsing the grade distribution from the LaTeX format
def parse_latex_table(input_str):
    values = input_str.strip().split("&")
    table = [int(val) for val in values]
    return np.array(table)

print("Bitte geben Sie die Übergangsmatrix ein. Beenden Sie die Eingabe mit 'enter'.")
matrix_input = input()
P = parse_latex_matrix(matrix_input)

for i, row in enumerate(P):
    if 'x' in row:
        x_index = row.index('x')
        x_value = 1.0 - sum([val for val in row if val != 'x'])
        P[i][x_index] = x_value

P = np.array(P)

print("Bitte geben Sie die Tabelle mit den Noten ein. Beenden Sie die Eingabe mit 'enter'.")
table_input = input()
grades = parse_latex_table(table_input)

grades_6 = np.round(np.linalg.matrix_power(P, 1).T @ grades).astype(int)
grades_7 = np.round(np.linalg.matrix_power(P, 2).T @ grades).astype(int)
grades_10 = np.linalg.matrix_power(P, 5).T @ (grades / np.sum(grades))

x = P[-1, 1]
num_students_6_grade_2 = grades_6[1]
num_students_7_grade_3 = grades_7[2]
prob_10_grade_4 = grades_10[3]

P3 = np.linalg.matrix_power(P, 3)
prob_7_grade_4_to_9_grade_4 = P3[3, 3]

print(f"Berechne den Wert x = {x:.2f}")
print(f"Auf dem Jahreszeugnis der 6. Klasse hatten {num_students_6_grade_2} Kinder die Note 2 in Mathematik")
print(f"Auf dem Jahreszeugnis der 7. Klasse hatten {num_students_7_grade_3} Kinder die Note 3 in Mathematik")
print(f"Die Wahrscheinlichkeit, dass eine zufällig ausgewählte Schülerin am Ende der 10. Klasse in Mathematik die Note 4 hat, liegt bei p = {prob_10_grade_4:.5f}")
print(f"Die Wahrscheinlichkeit, dass eine Schülerin, die am Ende der 7. Klasse die Note 4 hatte, am Ende der 9. Klasse die Note 4 hat, liegt bei q = {prob_7_grade_4_to_9_grade_4:.3f}")
