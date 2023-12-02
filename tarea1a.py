#orden de numeros#
print("===================================")
print("orden de numeros de mayor a menor: ")
print("===================================")
print("ingrese el primer numero: ")
num1=int(input())
print("ingrese el segundo numero: ")
num2=int(input())
print("ingrese el tercer numero; ")
num3=int(input())
if (num1>num2 and num2>3):
    print("",num1," , ",num2," , ",num3)
elif  (num2>num1 and num1>3):
    print("",num2," , ",num1," , ",num3)
elif (num3>num1 and num1>2):
    print("",num3," , ",num1," , ",num2)
elif  (num3>num2 and num2>1):
    print("",num3," , ",num2," , ",num1)
elif  (num1>num3 and num3>2):
    print("",num1," , ",num3," , ",num2)
elif  (num2>num3 and num3>1):
    print("",num2," , ",num3," , ",num1)
else:
    print("los numeros son iguales.")
    