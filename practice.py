first_num=int(input("Enter your first number"))
second_num=int(input("Enter your second"))
operator= input("Enter your operator(+,-,*,/ :)")
if operator =="+":
    result= first_num + second_num
    print(result)
elif operator =="-":
    resul =first_num - second_num
    print(result)
elif operator == "*":
    result = first_num * second_num
    print(result)
elif operator =="/":
    result = first_num / second_num
    print (result)
else:
    print("wrong operator")
