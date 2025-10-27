
# -  1. Write a program to define a function with multiple return values.
def main():
    number1= int(input('Enter a number: '))
    number2 = int(input('Enter another number: '))
    add,pro = result(number1,number2)
    print(f'the sum of {number1} and {number2} is: {add}')
    print(f'the product of {number1} and {number2} is: {pro}')


def result(num1,num2):
    return num1+num2,num1*num2

if __name__ == '__main__':
    main()

# -  2. Write a program to define a function using default arguments.
def main():
    name = input('Enter your name: ')
    print(print_name(name))
    print(print_name())


def print_name(name = "no name"):
    return f'Hello, {name}'
if __name__ == '__main__':
    main()


# -  3. Write a program to find the length of the string without using any library functions.
def main():
    string = input('Enter a string: ')
    length = 0
    for char in string:
        length += 1

    print("the length of string is ",length)
if __name__ == '__main__':
    main()

# -  4. Write a program to check if the substring is present in a given string or not.
def main():
    string = input('Enter a string: ')
    sub_string = input('Enter a substring: ')
    if sub_string in string:
        print("Yes substring is in string")
    else:
        print("substring not in string")
if __name__ == '__main__':
    main()

 # 5. Write a program to perform the given operations on a list:
 # i. addition
 # ii. Insertion
 # iii. slicing

def main():
    li = [1,2,3,4,5,6,7,8,9]

    print(li)
    number = int(input('Enter a number: '))
    li.append(number)  # adding
    print(li)
    number2 = int(input('Enter a number: '))
    li.insert(8,number2)
    print(li)
    print(li[3:7],"slicing from 3 to 7")  # slicing

if __name__ == '__main__':
    main()

# -  6. Write a program to perform any 5 built-in functions by taking any list.
def main():
    lis = [3,6,7,8,9,2,3,4,1,0]
    print(lis)
    minimum = min(lis)
    maximum = max(lis)
    total = sum(lis)
    length = len(lis)


    print("the length of list using len() is ",length )
    lis.sort()
    print("the sorted list using sort() is ",lis)
    print("the minimum in  list using min() is ",minimum )
    print("the maximum in  list using max() is ",maximum )
    print("the sum of list using sum() is ",total )
if __name__ == '__main__':
    main()
