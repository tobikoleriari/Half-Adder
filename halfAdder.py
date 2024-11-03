def half_adder(A, B):
    # XOR operation for Sum
    Sum = A ^ B
    # AND operation for Carry
    Carry = A & B
    return Sum, Carry

# Input: Two binary numbers (0 or 1)
A = int(input("Enter the first binary input (0 or 1): "))
B = int(input("Enter the second binary input (0 or 1): "))

# Ensure inputs are valid
if A in [0, 1] and B in [0, 1]:
    Sum, Carry = half_adder(A, B)
    print("Sum:", Sum)
    print("Carry:", Carry)
else:
    print("Invalid input. Please enter 0 or 1.")
