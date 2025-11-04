import numpy as np

# Function to input a matrix
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    # Input matrix dimensions
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Input matrices
    print("\nEnter elements for Matrix 1:")
    matrix1 = input_matrix(rows, cols)
    
    print("\nEnter elements for Matrix 2:")
    matrix2 = input_matrix(rows, cols)

    # Matrix Operations
    print("\nMatrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    # Addition
    print("\nMatrix Addition:")
    print(matrix1 + matrix2)

    # Subtraction
    print("\nMatrix Subtraction:")
    print(matrix1 - matrix2)

    # Multiplication (element-wise)
    print("\nMatrix Multiplication (element-wise):")
    print(matrix1 * matrix2)

    # Division (element-wise)
    print("\nMatrix Division (element-wise):")
    with np.errstate(divide='ignore', invalid='ignore'):
        result = matrix1 / matrix2
        result[result == np.inf] = 'Inf'  # Replace 'inf' with string 'Inf'
        print(result)

# Run the program
if __name__ == "__main__":
    main()
