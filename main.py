# from typing import Union


# def my_dummy_int_func(a: Union[str, float]) -> None:
#     try:
#         int_value = int(a)
#     except ValueError:
#         print('Value of "a" cannot be deduced to integer')
#     except TypeError:
#         print('Type of "a" is incompatible; should either be a number or a string')


# my_dummy_int_func("5")


# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
# exception ValueError:
# Raised when an operation or function receives an argument that has the right type but an inappropriate value,
# and the situation is not described by a more precise exception such as IndexError.

# from typing import Union


# a: int = input("Enter integer: ")

# def check_int(a: Union[int, str, float]) -> None:
#     try:
#         int_value: int = int(a)
#     except ValueError:
#         print("You've entered not an integer....")
#     else:
#         print("This is integer")

# print(check_int(a=a))

# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# exception FileNotFoundError:

# def calculate() -> float:
#     num_a: int = input("Enter first number: ")
#     if num_a.isnumeric():
#         num_a = int(num_a)
#     else:
#         raise TypeError("wrong Type.")
    
#     num_b: int = input("Enter second number: ")
#     if num_b.isnumeric():
#         num_b = int(num_b)
#     else:
#         raise TypeError("wrong Type.")
    
#     sign: str = input("Enter sign: ")
    
#     if sign == "+":
#         res = num_a + num_b
#     elif sign == "-":
#         res = num_a - num_b
#     elif sign == "*":
#         res = num_a * num_b
#     elif sign == "/":
#         res = num_a / num_b
#     else:
#         raise NameError("Wrong sign.")
#     return f"Result: {res}"

# try:
#     print(calculate())
# except TypeError:
#     print("Wrong Type...!")
# except NameError:
#     print("Wrong sign...!")


    