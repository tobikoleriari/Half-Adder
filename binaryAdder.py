def half_adder(A, B):
    # XOR operation for Sum
    Sum = A ^ B
    # AND operation for Carry
    Carry = A & B
    return Sum, Carry

def binary_adder(num1, num2):
    # Ensure both numbers are the same length by padding with zeros
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)


    result = ""
    carry = 0

    # Add each bit starting from the least significant bit
    for i in range(max_len - 1, -1, -1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        # First, add the two bits using a Half Adder
        sum_bit, carry_out = half_adder(bit1, bit2)

        # Now add the previous carry to the sum_bit using another Half Adder
        final_sum, new_carry = half_adder(sum_bit, carry)

        # Update carry for the next iteration
        carry = carry_out | new_carry

        # Prepend the sum result to the final result string
        result = str(final_sum) + result

    # If there is a carry left, add it to the result
    if carry:
        result = "1" + result

    return result

# Example binary numbers to add
binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

# Perform binary addition
output = binary_adder(binary1, binary2)
print("Result of binary addition:", output)
