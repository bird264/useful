#to run this code, copy it and run it in main.py
w = int(input("what type of numbers would you like to calculate? \n" + "P.S. Write the number for each! \n" + "1. integers \n" + "2. decimals/floats \n" + "3. fractions (for mixed numbers, make them improper) \n"))
if w == 1:
  num = int(input("how many numbers would you like to calculate? \n"))
  if num == 2:
    num_1 = int(input("what is your first number? \n"))
    num_2 = int(input("what is your second number? \n"))
    operation_1 = input("what operation would you like to use? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
    if operation_1 == "+":
      print(num_1 + num_2)

    if operation_1 == "-":
      print(num_1 - num_2)

    if operation_1 == "*":
      print(num_1 * num_2)

    if operation_1 == "/":
      print(num_1 / num_2)

  elif num == 3:
    num_1 = int(input("what is your first number? \n"))
    num_2 = int(input("what is your second number? \n"))
    num_3 = int(input("what is your third number? \n"))
    operation_1 = input("what is the first operation you would like to use? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
    operation_2 = input("what is the second operation you would like to use? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
    if operation_1 == "+":
      sum = num_1 + num_2

    if operation_1 == "-":
      sum = num_1 - num_2

    if operation_1 == "*":
      sum = num_1 * num_2

    if operation_1 == "/":
      sum = num_1 / num_2

    if operation_2 == "+":
      print(sum + num_3)

    if operation_2 == "-":
      print(sum - num_3)

    if operation_2 == "*":
      print(sum * num_3)

    if operation_2 == "/":
      print(sum / num_3)

  elif num == 4:
    num_1 = int(input("what is your first number? \n"))
    num_2 = int(input("what is your second number? \n"))
    num_3 = int(input("what is your third number? \n"))
    num_4 = int(input("what is your fourth number? \n"))
    operation_1 = input("what is the first operation you would like to use? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
    operation_2 = input("what is the second operation you would like to use? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
    operation_3 = input("what is the third operation you would like to use? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
    if operation_1 == "+":
      sum = num_1 + num_2

    if operation_1 == "-":
      sum = num_1 - num_2

    if operation_1 == "*":
      sum = num_1 * num_2

    if operation_1 == "/":
      sum = num_1 / num_2

    if operation_2 == "+":
      sum_2 = sum + num_3

    if operation_2 == "-":
      sum_2 = sum - num_3

    if operation_2 == "*":
      sum_2 = sum * num_3

    if operation_2 == "/":
      sum_2 = sum / num_3

    if operation_3 == "+":
      print(sum_2 + num_4)

    if operation_3 == "*":
      print(sum_2 * num_4)

    if operation_3 == "/":
      print(sum_2 + num_4)

    if operation_3 == "-":
      print(sum_2 + num_4)

    else:
      print("unidentified integer, please rerun code.")
      exit(0)
  elif num == 1:
    print("please rerun code and enter a number greater than 1.")
    exit(0)

  else:
    print("sorry, this calculator can only calculate up to 4 numbers.")
    exit(0)

elif w == 2:
  num = float(input("write down the first decimal/float that you would liek to calculate \n"))
  num1 = float(input("write down the second decimal/float that you would like to calculate \n"))
  operation = input("what operation would you like to use on these numbers? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")
  if operation == "+":
    print(num + num1)

  elif operation == "-":
    print(num - num1)

  elif operation == "*":
    print(num * num1)

  elif operation == "/":
    print(num / num1)

elif w == 3:
  num = int(input("what is the numerator of your first fraction? \n"))
  num1 = int(input("what is the denominator of your first fraction? \n"))
  num2 = int(input("what is the numerator of your second fraction? \n"))
  num3 = int(input("what is the denominator of your second fraction? \n"))
  operation = input("what operation would you like to use on these fractions? \n" + "1. + \n" + "2. - \n" + "3. * \n" + "4. / \n")

  if operation == "+":
    print(num * num3 + num1 * num2)
    print("---")
    print(num1 * num3)

  elif operation == "-":
    print(num * num3 - num1 * num2)
    print("---")
    print(num1 * num3)

  elif operation == "*":
    print(num * num2)
    print("---")
    print(num1 * num3)

  elif operation == "/":
    print(num * num3)
    print("---")
    print(num1 * num2)
else:
  print("please rerun code, unidentified answer")
  exit(0)
