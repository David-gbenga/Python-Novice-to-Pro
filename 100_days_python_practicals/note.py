#How to manage out of  index errors in Python
my_list = [10, 20, 30, 40, 50]
#Always check the length of the list before accessing an index
list_length = len(my_list)
#Try to subtract 1 from the length to get the last valid index
last_index = list_length - 1
print(f"The last valid index is: {last_index}")


#How to manage lengthy list that can be grouped
lit_food = ["apple", "banana", "cherry", "date", "rice", "beans","elderberry", "fig", "grape"]
#Group the list into sublists of 2 items each
food_list = ["rice", "beans"]
fruit = ["apple", "banana", "cherry", "date","elderberry", "fig", "grape"]
lit_food = [food_list, fruit]
print(lit_food)