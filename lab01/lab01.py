def gcd(a, b):

 while b:
  a, b = b, a % b
 return a

try:
 num1 = int(input("Введите первое число: "))
 num2 = int(input("Введите второе число: "))

 if num1 == 0 and num2 == 0:
  print("НОД не может быть определен, так как оба числа равны нулю.")
 else:
  result = gcd(num1, num2)
  print("НОД:", result)

except ValueError:
 print("Ошибка: Введены некорректные числа. Пожалуйста, введите целые числа.")
