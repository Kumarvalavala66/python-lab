
#  6. Create a dictionary with at least five keys and each key represent value as a list where this list contains at least ten values and convert this dictionary as a pandas data frame and explore the data:
# ◦ a) Apply head () function to the pandas data frame
# ◦ b) Perform various data selection operations on Data Frame
#  7. Select any two columns from the above data frame, and observe the change in one attribute with respect to other attribute with scatter and plot operations in matplotlib




#  1. Python program to check whether a JSON string contains complex object or not.

import json

json_str = '''
    {
        "student": {
            "name": "Prasanna",
            "age": 21,
            "courses": ["Python", "AI", "Math"],
            "address": {
                "city": "Hyderabad",
                "pin code": 500081
            }
        }
    }
    '''
def is_complex_obj(obj):
    if isinstance(obj, dict):
        return True
    if isinstance(obj, list):
        for item in obj:
            if  is_complex_obj(item):
                return True
    return False

def main():
    data = json.loads(json_str)
    if is_complex_obj(data):
        print("is complex")
    else:
        print("is not complex")
if __name__ == '__main__':
    main()

#  2. Python Program to demonstrate NumPy arrays creation using array () function.
import numpy as np
def main():
    arr1d = np.array([1, 2, 3, 4, 5])
    arr2d= np.array([[1, 2, 3, 4, 5]
                    ,[6,7,8,9,0,]])
    arr3d= np.array([[1, 2, 3, 4, 5]
                    ,[6,7,8,9,0,],
                    [1,2,3,4,5]])
    print(arr1d,"\n the dimensions of array is ",arr1d.ndim)
    print(arr2d,"\n the dimensions of array is ",arr2d.ndim)
    print(arr3d,"\n the dimensions of array is ",arr3d.ndim)

if __name__ == '__main__':
    main()

#  3. Python program to demonstrate use of ndim, shape, size, dtype.
import numpy as np
def main():
    arr = np.random.randint(10,size=(3,3) )
    print("The arry using is \n",arr)
    print("To find the Dimensions of an array use \"arr.ndim \" is ",arr.ndim)
    print("To find the Shape of an array use \"arr.shape \" is ",arr.shape)
    print("To find the Size of an array use \"arr.size \" is ",arr.size)
    print("To find the Data type of an array use \"arr.dtype \" is ",arr.dtype)


if __name__ == '__main__':
    main()

#  4. Python program to demonstrate basic slicing, integer and Boolean indexing.
import numpy as np
def main():
    arr_1d = np.array([1,2,3,4,5,6,7,8,9,10])
    print("The 1D array using for slicing is ",arr_1d)
    print("The array after slicing from possition 2 and 6 is ",arr_1d[1:6])

    arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    print("The 2D array using for slicing is ", arr_2d)
    print("The array after slicing second row 8 to 10 \n",arr_2d[1:2,2:5])

    print("Boolean indexing for 1D array and getting all even numbers ",arr_1d[arr_1d%2==0])

if __name__ == '__main__':
    main()

 # 5. Python program to find min, max, sum, cumulative sum of array.
import numpy as np


def main():
    arr = np.array([1, 2, 3 , 4 , 5 , 6, 7, 8, 9])
    print("The array using is ", arr)
    print("The maximum value in the array is found using max() ", np.max(arr))
    print("The minimum value in the array is found using min() ", np.min(arr))
    print("The sum  of elements the array is found using max() ", np.sum(arr))
    print("The cumulative value in the array is found using cumsum() ", np.cumsum(arr))

if __name__ == '__main__':
    main()

# - [ ] 6. Create a dictionary with at least five keys and each key represent
# value as a list where this list contains at least ten values and convert this dictionary
# as a pandas data frame and explore the data:
#  a) Apply head () function to the pandas data frame
# b) Perform various data selection operations on Data Frame
import pandas as pd
def main():
    data = {
        "name" : ["Prasanna","Kumar","Jaswanth","Willi","Harshit","Statlin","Manoj","Suhas","Devi","Prasad"],
        "age" :[22,23,22,24,21,25,23,22,23,22],
        "CGPA" : [9.9,9.8,8.8,9.0,7.6,8.9,9.0,7.9,8.0,9.0],
        "collage" : ["BVC","BVC","SRKR","BVC","BVC","BVC","ADITHYA","BVC","BVC","NNB"],
        "grade" : ["A","B","C","B","A","B","C","D","B","A"],
    }

    li = [i for i in range(1,11)]
    df = pd.DataFrame(data,index =li )
    print("the original data is \n",df)
    print("the new data after the applying head() for first 5  \n",df.head(5))
    less = df[df["CGPA"] < 9.0]
    print("the people scored less than 9.0 \n",less["name"])
    print("the top scocers is \n",df.sort_values(by="CGPA", ascending=False).head(5))


if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary with five keys and each key has a list of ten values
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Desktop', 'Smartwatch',
                'Camera', 'Headphones', 'Speaker', 'Monitor', 'Keyboard'],
    'Price': [1000, 800, 300, 1200, 200, 150, 250, 100, 400, 80],
    'Stock': [20, 50, 30, 15, 100, 60, 80, 40, 25, 200],
    'Rating': [4.5, 4.7, 4.3, 4.6, 4.2, 4.8, 4.1, 4.5, 4.3, 4.0],
    'Brand': ['Dell', 'Apple', 'Samsung', 'HP', 'Fossil',
              'Canon', 'Sony', 'JBL', 'LG', 'Logitech']
}


df = pd.DataFrame(data)


x = df['Price']
y = df['Rating']


plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7, s=100)


plt.title('Scatter Plot of Price vs Rating', fontsize=16)
plt.xlabel('Price ($)', fontsize=14)
plt.ylabel('Rating (out of 5)', fontsize=14)
plt.grid(True)


plt.show()

