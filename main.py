from utils.binary_utils import decimal_to_binary, binary_to_decimal
from adders.eight_bit_adder import eight_bit_adder

def add_interface(num1, num2):

    binary_num1 = decimal_to_binary(num1)
    binary_num2 = decimal_to_binary(num2)

    print(f"Number 1 in Decimal: {num1}, Binary: {binary_num1}")
    print(f"Number 2 in Decimal: {num2}, Binary: {binary_num2}")
    print("-------------------------------------")

    # Convert binary strings to lists of integers
    binary_num1_list = list(map(int, binary_num1))
    binary_num2_list = list(map(int, binary_num2))

    result = eight_bit_adder(binary_num1_list, binary_num2_list)
    binary_result = ''.join(map(str, result))
    decimal_result = binary_to_decimal(binary_result)

    print(f"Sum :: Decimal: {decimal_result}, Binary: {binary_result}")

def user_interface():
    try:
        num1 = int(input("Enter the first number (0-255): "))
        num2 = int(input("Enter the second number (0-255): "))
        print("-------------------------------------")

        if 0 <= num1 <= 255 and 0 <= num2 <= 255:
            add_interface(num1, num2)
        else:
            print("Error: Please enter numbers in the range 0-255.")

    except ValueError:
        print("-------------------------------------")
        print("Invalid input! Please enter a valid integer.")

def main():
    user_interface()

if __name__ == "__main__":
    main()