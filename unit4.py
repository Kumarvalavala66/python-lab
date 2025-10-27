
# Write a program to sort words in a file and put them in another file. The output file should have only lower-case words, so any upper-case words from source must be lowered.
def main():
    file = "normal.txt"
    with open(file,'r') as f:
        content = f.read()
    words = content.split()
    words = [word.lower() for word in words]
    words = " ".join(words)

    with open('output.txt','w') as f:
        f.write(words)
if __name__ == '__main__':
    main()

#  2. Python program to print each line of a file in reverse order.
def main():
    file = "file.txt"
    with open(file ,'r') as f:
        content= f.readlines()
        line_content = content
    with open(file,'w') as f:
        for line in line_content:
            f.write(line[::-1])


if __name__ == '__main__':
    main()

#  3.Python program to compute the number of characters, words and lines in a file.
def main():
    file = "file.txt"
    with open(file,'r') as f:
        lines = f.readlines()
    lines_count = len(lines)
    for line in lines:
        words_count = len(line.split())
        letters_count = len(line)


    print("The number of lines in the file is:", lines_count)
    print("The number of words in the file is:", words_count)
    print("The number of characters in the file is:", letters_count)



if __name__ == '__main__':
    main()


# 4. Write a program to create, display, append, insert and reverse the order of the items in the array.
def main():
    my_list = [1, 2, 3,4,5,6,7]
    print(my_list)
    num = int(input('Enter a number to append : '))
    my_list.append(num)
    print("After appending ",num," in to list ",my_list)
    num1 = int(input('Enter a number to insert at 3rd idx: '))
    my_list.insert(3,num1)
    print("After inserting ",num1," in to list ",my_list)
    my_list.reverse()
    print("the reverse order is ",my_list)

if __name__ == '__main__':
    main()


# Write a program to add, transpose and multiply two matrices.
import numpy as np
def main():
    arr = np.random.randint(1,10 , size=(3,3))
    print(arr)
    arr1 = np.random.randint(1,10 , size=(3,3))
    print(arr1)
    print("the sum of both arr1 and arr2 is \n", arr + arr1)
    print("the multiplication  of both arr1 and arr2 is \n", arr @ arr1)
    print("the transpose of arr1  is \n", arr.T,"\n and  arr 2 is \n",arr1.T )


if __name__ == '__main__':
    main()



#  6. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + self.width
class Circle(Shape):
    def __init__(self, radius):

        self.radius = radius
    def area(self):
        return   math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, lenght, base, height):
        self.lenght = lenght
        self.base = base
        self.height = height
    def area(self):
        return .5 * self.lenght * self.base * self.height
    def perimeter(self):
        return self.lenght + self.base + self.height
def main():
    rectangle = Rectangle(10, 20)
    area = rectangle.area()
    perimeter = rectangle.perimeter()
    print("The area of Rectangle is ",area)
    print("The perimeter of Rectangle is ",perimeter)

    circle = Circle(10)
    area = circle.area()
    perimeter = circle.perimeter()
    print(f"The area of Circle is{area:.2f} ")
    print(f"The perimeter of Circle is {perimeter:.2f}")

    triangle = Triangle(10, 20, 30)
    area = triangle.area()
    perimeter = triangle.perimeter()
    print("The area of Triangle is ",area)
    print("The perimeter  of Triangle is ",perimeter)

if __name__ == '__main__':
    main()
