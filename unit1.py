import operator



#  6. Write a program to print multiplication table of a given number.

# #  1. Write a program to find the largest element among three Numbers.
#
#
# def largest(num1, num2, num3):
#     large = num1
#     if num2 > large:
#         large = num2
#     if num3 > large:
#         large = num3
#     return large
# def main():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     num3 = int(input("Enter the third number: "))
#     result = largest(num1, num2, num3)
#     print(f"the largest number among {num1}, {num2}, {num3} is: {result}")
# if __name__ == '__main__':
#     main()


# #  2. Write a Program to display all prime numbers within an interval.
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     else: return True
#
# def main():
#     start = int(input('Enter starting  number: '))
#     end = int(input('Enter ending  number: '))
#     for i in range(start, end+1):
#         if is_prime(i):
#             print(i)
# if __name__ == '__main__':
#     main()

# #  3. Write a program to swap two numbers without using a temporary variable
# def main():
#     num1 = int(input('Enter a number: '))
#     num2 = int(input('Enter another number: '))
#     print(f"Before swapping num1 : {num1}, num2 : {num2} ")
#     num1 = num2 + num1
#     num2 = num1 - num2
#     num1 = num1 - num2
#     # this can also get work done in python
#     # num1,num2 = num2 ,num1
#     print(f"After swapping num1 : {num1}, num2 : {num2} ")
# if __name__ == '__main__':
#     main()


#  4. Demonstrate the following Operators in Python with suitable examples:
 # Arithmetic Operators
 # ii) Relational Operators
 # iii) Assignment Operators
 # iv) Logical Operators
 # v) Bitwise Operators
 # vi) Ternary Operator
 # vii) Membership Operators
 # viii) Identity Operators
#
# def main():
#      num1 = int(input('Enter  number 1 : '))
#      num2 = int(input('Enter  number 2: '))
#      print("Arithmetic Operators")
#      print(f"num1 + num2 = {num1+num2}")
#      print(f"num1 - num2 = {num1-num2}")
#      print(f"num1 / num2 = {num1/num2}")
#      print(f"num1 * num2 = {num1*num2}")
#      print(f"num1 // num2 = {num1//num2}")
#      print(f"num1 ** num2 = {num1**num2}")
#      print(f"num1 % num2 = {num1%num2}")
#
#      print("Relational Operators")
#      print(f"num1 == num2 : {num1==num2}")
#      print(f"num1 < num2 : {num1<num2}")
#      print(f"num1 > num2 : {num1>num2}")
#      print(f"num1 <= num2 : {num1<=num2}")
#      print(f"num1 >= num2 : {num1>=num2}")
#
#      print("Assignment Operators")
#      temp1 = num1
#      temp2 = num2
#      temp1 += temp2
#      print(f"num1 += num2 : {temp1}")
#      temp1 = num1
#      temp2 = num2
#      temp1 -= temp2
#      print(f"num1 -= num2 : {temp1}")
#      temp1 = num1
#      temp2 = num2
#      temp1 *= temp2
#      print(f"num1 *= num2 : {temp1}")
#
#      temp1 = num1
#      temp2 = num2
#      temp1 /= temp2
#      print(f"num1 /= num2 : {temp1}")
#      print("Logical Operators")
#      val1 = True
#      val2 = False
#      print(f'val1 = {val1} val2 = {val2}')
#      print(f'val1 and val2= {val1 and val2}')
#      print(f'val1 or val2= {val1 or val2}')
#      print(f'not val1 = {not val1 }')
#      print(f'not val2 = {not val2 }')
#
#      print("Ternary Operator")
#      print("if num1 < num2 print num1 else num2",num2 if num1 < num2 else num1 )
#
#      print(" Membership Operators")
#      li = [1,2,3,4,5]
#      print("[1,2,3,4,5] is list \n if 2 in list ",2 in li )
#      print(" if 2 not in list ",2 not in li )
#
#      print("Identity Operators")
#      print("num1 is num2",num1 is num2)
#      print("num1 is not num2",num1 is not num2)
#
# if __name__ == '__main__':
#     main()

#
# #  5. Write a program to add and multiply complex numbers.
# def main():
#     a = int(input("num1 real part :"))
#     b= int(input("num1 imaginary part :"))
#
#     c =  int(input("num2 real part :"))
#     d = int(input("num2 imaginary part :"))
#
#     result_real = (a*c - b*d)
#     result_img = (a*d + b*c)
#     sum_real = a+c
#     sum_img = b+d
#     print(f"the product of complex numbers ({a}+i{b}) and ({c}+i{d}) is ({result_real}+{result_img}i)")
#     print(f"the sum of complex numbers ({a}+i{b}) and ({c}+i{d}) is ({sum_real}+i{sum_img})")
# if __name__ == '__main__':
#     main()

def main():
    number = int(input('Enter a number: '))
    limit = int(input('Enter a limit: '))
    for num in range(1,limit+1):
        print(f"{number} x {num} = {number*num}")

if __name__ == '__main__':
    main()