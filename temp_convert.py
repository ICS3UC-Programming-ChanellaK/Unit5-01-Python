# #!/usr/bin/env python3
# Created By: Chanella
# Date: May 5, 2025
# This program converts temperature to fahrenheit from celsius
#
def calculate_temp():
    # calculate temperature
    try:
        # ask the user to enter the temperature in celsius
        celsius = float(input("Enter the temperature in celsius: "))

        # convert celsius to fahrenheit
        fahrenheit = (celsius * 9 / 5) + 32
        print("The temperature in fahrenheit is :", fahrenheit)

    except ValueError:
        print("Invalid,Please enter a valid temperature!")

def main ():
    # the function calls the other function
    calculate_temp()
if __name__ == "__main__":
    # call the  main function
    main()
