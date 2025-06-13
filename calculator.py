num1=float(input("Enter num1 value:"))
num2=float(input("Enter num2 value:"))
operator=input("Enter a operator:")
if operator=='+':
    print(f"addition of num1 and num2 is:{round(num1+num2,2)}")
elif operator=='-':
    print(f"subtraction of num1 and num2 is:{round(num1-num2,2)}")
elif operator=='*':
    print(f"multiplication of num1 and num2 is:{round(num1*num2,2)}")
elif operator=='/':
    if num2!=0:
      print(f"division of num1 and num2 is:{round(num1/num2,2)}")
    else:
        print("Error:Division by zero is not allowed")
else:
    print("not a valid operator")