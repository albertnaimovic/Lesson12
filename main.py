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

############################################### PAVYZDYS KAIP NAUDOTI IR NEPRASIPISTI###################################################


# def divide_two_numbers(dividend: int, divisor: int) -> None:
#     try:
#         return dividend / divisor
#     except Exception as err:
#         print(f'You got {err} error!')

# def power(a, b):
#     answer_number = divide_two_numbers(a, b)
#     if not answer_number:
#         return 0
#     return answer_number ** 2

# # print(divide_two_numbers(1, 0))
# print(power(1, 2))

#########################################################################################################################################

# Create a program which takes a sentence as your birth date (YYYY:MM:DD)
# The program should return sum of all numbers, bigest and lowest number division
# and days with power of month (dd ** mm)
# The code should be structured correctly: functions, error handling and logging.

from typing import List
import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="1_task.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def format_date_string(my_date: str) -> list:
    try:
        datetime.datetime.strptime(my_date, "%Y:%m:%d")
    except Exception as err:
        logging.error(f"You got {err} error!")
    else:
        number_list = [int(x) for x in my_date if x.isnumeric()]
        return number_list


def sum_numbers(number_list: List[int]) -> int:
    # try:
    suma = sum(number_list)
    return suma


# except Exception as err:
# logging.error(f'You got {err} error!')


def divide_two_numbers(number_list: List[int]) -> float:
    # try:
    return max(number_list) / min(number_list)


# except Exception as err:
# logging.error(f'You got {err} error!')


def days_power_month(number_list: str) -> int:
    dd = int("" + (str(number_list[6])) + str(number_list[7]))
    mm = int("" + (str(number_list[4])) + str(number_list[5]))
    # try:
    return dd**mm
    # except Exception as err:
    # logging.error(f'You got {err} error!')


my_date: str = "1997:10:09"  # input("Enter your date of birth (YYYY:MM:DD): ")

try:
    number_list: list = format_date_string(my_date)
    suma = sum_numbers(number_list)
    power = days_power_month(number_list)
    divided_nums = divide_two_numbers(number_list)
    print(f"Sum: {suma}\nDivision: {divided_nums}\nPower: {power}")
except Exception as err:
    logging.error(f"You got {err} error!")
