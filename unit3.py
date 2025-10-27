



#

# # - [ ] 1. Write a program to create tuples (name, age, address, college) for
# # at least two members and concatenate the tuples and print the concatenated tuples.
# def main():
#     data1 = ("kumar",18,"kanakayalanka","BVC")
#     data2 = ("Manoj",19,"Nagaram","BVC")
#     full_data = data1 + data2
#     print(full_data)
#
#
#
# if __name__ == '__main__':
#     main()

# # - [ ] 2. Write a program to count the number of vowels in a string (No control flow allowed).
# def main():
#     string = input('Enter a string: ')
#     vowels = "aeiouAEIOU"
#     count = sum(map(string.count, vowels))
#     print("the number of vowels is: ", count)
# if __name__ == '__main__':
#     main()

# # - [ ] 3. Write a program to check if a given key exists in a dictionary or not.
# def main():
#     di = {
#         "name": 1,
#         "age": 2,
#         "address": 3,
#         "clg": 4, }
#     val = input("Enter key to search for: ").strip()
#     if val in di:
#         print("the key is found ")
#     else:
#         print("key not found")
# if __name__ == '__main__':
#     main()

# - [ ] 4. Write a program to add a new key-value pair to an existing dictionary.
# def main():
#     di = {
#         "name": 1,
#         "age": 2,
#         "address": 3,
#         "clg": 4,
#     }
#     print(di)
#     key = input("Enter a key: ")
#     value = (input("Enter a value: "))
#     di[key] = value
#     print(di)
# if __name__ == '__main__':
#     main()


# 5.Write a program to sum all the items in a given dictionary.
def main():
    di = {
            "name": 1,
            "age": 2,
            "address": 3,
            "clg": 4,
            "pro": 5,
             "som":6
        }
    result = sum(di.values())
    print(result)
if __name__ == '__main__':
    main()