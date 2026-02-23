num1 = float(input ("Please enter the first number. "))
num2 = float(input ("Please enter the second number. "))
choice = int(input ("Choose the operation you want to perform from below. Pick the number next to your desired operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Floor Division\n7. Exponent/Power\n"))
Result = None

if choice == 1:
    Result = num1 + num2
elif choice == 2:
    Result = num1 - num2
elif choice == 3:
    Result = num1 * num2
elif choice == 4:
    Result = num1 / num2
elif choice == 5:
    Result = num1 % num2
elif choice == 6:
    Result = num1 // num2
elif choice == 7:
    Result = num1 ** num2
else:
    Result = None
    print ("Please enter one of the numbers.")

if Result != None:
    print (Result)