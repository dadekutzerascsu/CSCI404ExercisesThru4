def gauss_3m_multiply(a, b, c, d):
    """
    Multiplies (a + bi) * (c + di) using Gauss's 3M method.
    Requires exactly 3 multiplications and 5 additions/subtractions.
    """
    # Step 1: Compute the 3 multiplications
    P1 = a * c
    P2 = b * d
    P3 = (a + b) * (c + d)
    
    # Step 2: Combine using additions/subtractions
    real_part = P1 - P2
    imag_part = P3 - P1 - P2
    
    return real_part, imag_part


if __name__ == "__main__":
    print("--- Gauss Complex '3M' Multiplication Tool ---")
    print("Format: (a + bi) * (c + di)\n")
    
    # Collect components for the first complex number
    while True:
        try:
            a = float(input("Enter real part 'a': "))
            b = float(input("Enter imaginary part 'b': "))
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
    # Collect components for the second complex number
    while True:
        try:
            c = float(input("\nEnter real part 'c': "))
            d = float(input("Enter imaginary part 'd': "))
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
    # Calculate the product
    real, imag = gauss_3m_multiply(a, b, c, d)
    
    # Format whole numbers nicely for display
    a_str = f"{int(a)}" if a.is_integer() else f"{a}"
    b_str = f"{int(b)}" if b.is_integer() else f"{b}"
    c_str = f"{int(c)}" if c.is_integer() else f"{c}"
    d_str = f"{int(d)}" if d.is_integer() else f"{d}"
    
    real_str = f"{int(real)}" if real.is_integer() else f"{real}"
    imag_str = f"{int(imag)}" if imag.is_integer() else f"{imag}"
    
    # Display step-by-step intermediate terms
    print("\n==============================")
    print("Intermediate Gauss Products:")
    print("==============================")
    print(f"P1 = a * c = {real_str if real.is_integer() else real}") # Just to see P1, P2, P3 values
    print(f"P1 (a*c) = {a * c}")
    print(f"P2 (b*d) = {b * d}")
    print(f"P3 ((a+b)*(c+d)) = {(a + b) * (c + d)}")
    
    print("\n==============================")
    print("Final Result:")
    print("==============================")
    sign = "+" if imag >= 0 else "-"
    print(f"({a_str} + {b_str}i) * ({c_str} + {d_str}i) = {real_str} {sign} {abs(float(imag_str)) if '.' in imag_str else abs(int(imag_str))}i")
