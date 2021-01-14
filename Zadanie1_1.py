operators =  ["+", "-", "*", "/"]

str = input("Введите выражение:\n")

try:
    for item in operators:
        if str.find(item) != -1:
            operator_index = str.find(item)
            operator = str[operator_index]
            break

    num1 = str[:operator_index].strip()
    num2 = str[operator_index+1:].strip()

    if operator == "+":
        result = int(num1) + int(num2)
        print(f"Ответ: {result}")

    if operator == "-":
        result = int(num1) - int(num2)
        print(f"Ответ: {result}")

    if operator == "*":
        result = int(num1) * int(num2)
        print(f"Ответ: {result}")

    if operator == "/":
        if int(num2) > 0:
            result = int(num1) / int(num2)
            print(f"Ответ: {result}")
        else:
            print("Ошибка! Делитель должен быть больше нуля.")
except:
    print("Ошибка! Вы некорректно ввели выражение.")
    
        


