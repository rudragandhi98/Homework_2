# Create a Python project to get the value of Pi to n number of decimal places.
import math
while True:
    try:
        # Ask the user to input n
        user_input = int(input("Please input an integer n, to get n number of decimal places: "))
        approx_pi_fp = lambda x: round(math.pi , x)
        print(approx_pi_fp(user_input))
        break
    except ValueError:
        # If the user does not enter a integer then ask them to try again
        print("That was not a valid number. Please enter a number. Try again...")