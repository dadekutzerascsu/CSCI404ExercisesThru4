def add(A, B):
    """Adds two matrices."""
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def sub(A, B):
    """Subtracts two matrices."""
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def split(matrix):
    """Splits a square matrix into four quadrants."""
    n = len(matrix)
    mid = n // 2
    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bot_left = [row[:mid] for row in matrix[mid:]]
    bot_right = [row[mid:] for row in matrix[mid:]]
    return top_left, top_right, bot_left, bot_right


def winograd_strassen(A, B):
    """Recursive Winograd variant of Strassen's algorithm."""
    n = len(A)

    # Base Case: safely extract numerical values for 1x1 matrices
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Step 1: Subdivide matrices into quadrants
    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    # Step 2: Compute the 8 intermediate addition/subtraction matrices
    S1 = add(A21, A22)
    S2 = sub(S1, A11)
    S3 = sub(A11, A21)
    S4 = sub(A12, S2)
    S5 = sub(B12, B11)
    S6 = sub(B22, S5)
    S7 = sub(B22, B12)
    S8 = sub(S6, B21)

    # Step 3: Compute the 7 recursive matrix multiplications
    M1 = winograd_strassen(S2, S6)
    M2 = winograd_strassen(A11, B11)
    M3 = winograd_strassen(A12, B21)
    M4 = winograd_strassen(S3, S7)
    M5 = winograd_strassen(S1, S5)
    M6 = winograd_strassen(S4, B22)
    M7 = winograd_strassen(A22, S8)

    # Step 4: Combine multiplications using intermediate sum variables
    T1 = add(M1, M2)
    T2 = add(T1, M4)

    # Step 5: Construct the final 4 quadrants of result matrix C
    C11 = add(M2, M3)
    C12 = add(add(T1, M5), M6)
    C21 = sub(T2, M7)
    C22 = add(T2, M5)

    # Step 6: Merge quadrants into a single output matrix
    result = []
    for i in range(len(C11)):
        result.append(C11[i] + C12[i])
    for i in range(len(C21)):
        result.append(C21[i] + C22[i])

    return result


def get_matrix_input(name, n):
    """Prompts user to type a square matrix line-by-line."""
    print(f"\nEnter the rows for Matrix {name} ({n}x{n}):")
    print("Type space-separated numbers for each row, then press Enter.")
    matrix = []
    for i in range(n):
        while True:
            try:
                row_input = input(f"Row {i+1}: ")
                row = [float(x) for x in row_input.split()]
                if len(row) != n:
                    print(
                        f"Error: Row must have exactly {n} elements. Try again."
                    )
                    continue
                # Clean formatting for whole integers
                row = [int(x) if x.is_integer() else x for x in row]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
    return matrix


# =====================================================================
# Interactive Driver Execution
# =====================================================================
if __name__ == "__main__":
    print("--- Winograd-Strassen Matrix Multiplication Tool ---")

    while True:
        try:
            n_input = input(
                "Enter the matrix size 'n' (must be a power of 2, e.g., 2, 4, 8): "
            )
            n = int(n_input)
            if n <= 0 or (n & (n - 1)) != 0:
                print("Error: The size must be a positive power of 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Collect user arrays
    matrix_A = get_matrix_input("A", n)
    matrix_B = get_matrix_input("B", n)

    # Process and print output
    try:
        result = winograd_strassen(matrix_A, matrix_B)
        print("\n==============================")
        print("Computed Product via Winograd-Strassen:")
        print("==============================")
        for row in result:
            print(row)
    except Exception as e:
        print(f"\nAn error occurred during calculation: {e}")
