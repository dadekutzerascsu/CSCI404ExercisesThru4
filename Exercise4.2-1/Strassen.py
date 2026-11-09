def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def split(matrix):
    n = len(matrix)
    mid = n // 2
    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bot_left = [row[:mid] for row in matrix[mid:]]
    bot_right = [row[mid:] for row in matrix[mid:]]
    return top_left, top_right, bot_left, bot_right


def merge(C11, C12, C21, C22):
    matrix = []
    for i in range(len(C11)):
        matrix.append(C11[i] + C12[i])
    for i in range(len(C21)):
        matrix.append(C21[i] + C22[i])
    return matrix


def strassen(A, B):
    n = len(A)

    # FIXED BASE CASE: Safely extract scalar elements for 1x1 computation
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    P1 = strassen(A11, sub(B12, B22))
    P2 = strassen(add(A11, A12), B22)
    P3 = strassen(add(A21, A22), B11)
    P4 = strassen(A22, sub(B21, B11))
    P5 = strassen(add(A11, A22), add(B11, B22))
    P6 = strassen(sub(A12, A22), add(B21, B22))
    P7 = strassen(sub(A11, A21), add(B11, B12))

    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)

    return merge(C11, C12, C21, C22)


def get_matrix_input(name, n):
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
                row = [int(x) if x.is_integer() else x for x in row]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
    return matrix


if __name__ == "__main__":
    print("--- Strassen Matrix Multiplication Interactive Tool ---")

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

    matrix_A = get_matrix_input("A", n)
    matrix_B = get_matrix_input("B", n)

    try:
        result = strassen(matrix_A, matrix_B)
        print("\n==============================")
        print("Computed Matrix Product Result:")
        print("==============================")
        for row in result:
            print(row)
    except Exception as e:
        print(f"\nAn error occurred during calculation: {e}")
