def pascal_element(r, c):

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    def binomial_coefficient(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    return binomial_coefficient(r, c)


# Example usage
row = 3
column = 2
element = pascal_element(row, column)
print(f"The element at position ({row}, {column}) is: {element}")


# variation-2

def pascal_row(n):
    row = []
    for i in range(n+1):
        # creating a row list and appending coefficients (using above function)
        row.append(pascal_element(n, i))
    return row


# Example usage
row_number = 5
row = pascal_row(row_number)
print(f"The {row_number}-th row of Pascal's triangle is: {row}")

# variation-3


def pascal_triangle(n):
    triangle = []
    for i in range(n):
        # creating a triangle list and appending rows (using above function)
        triangle.append(pascal_row(i))
    return triangle


# Example usage
num_rows = 4
triangle = pascal_triangle(num_rows)
print(f"The Pascal's triangle with {num_rows} rows is:")
for row in triangle:
    print(row)
