# [1,2,3,4] => [24,12,8,6]

def multiply_elements(array):
    result = 1
    for element in array:
        result *= element

    output = []
    for i in range(1, len(array)+1):
        output.append(result//i)

    return output


# Example usage
my_array = [1, 2, 3, 4]
produc = multiply_elements(my_array)

print("Product:", produc)
