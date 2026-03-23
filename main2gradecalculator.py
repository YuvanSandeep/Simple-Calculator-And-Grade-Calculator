Percentage = int(input("Enter your percentage."))

if Percentage > 89 and Percentage < 101:
    print ("You have an A grade")
elif Percentage > 79 and Percentage < 90:
    print ("You have a B grade")
elif Percentage > 69 and Percentage < 80:
    print ("You have a C grade")
elif Percentage > 59 and Percentage < 70:
    print ("You have a D grade")
elif Percentage > 100 or Percentage < 0:
    print ("Please enter a valid percentage.")
else:
    print ("You have an F grade")
