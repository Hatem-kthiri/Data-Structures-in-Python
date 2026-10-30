# Python Checkpoint

# Question 1: Multiplying List Items

numbers = [2, 3, 6]

result = 1

for number in numbers:
    result *= number

print("Question 1:", result)


# Question 2: Sorting Tuples by the Last Element

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

result = []

while my_list:
    smallest = my_list[0]

    for item in my_list:
        if item[-1] < smallest[-1]:
            smallest = item

    result.append(smallest)
    my_list.remove(smallest)

print(result)


# Question 3: Combining Dictionaries

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()

for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print("Question 3:", result)


# Question 4: Creating a Dictionary of Squares

n = int(input("Question 4 - Enter an integer: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Question 4:", squares)


# Question 5: Sorting Tuples by a Float Value

list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

result = []

while list: 
    largest = list[0]

    for item in list:
       if float(item[-1]) > float(largest[-1]):
           largest = item

    result.append(largest)
    list.remove(largest)
print(result)


# Question 6: Creating a Set

numbers = {0, 1, 2, 3, 4}

print("Question 6A:", numbers)


# Question 6: Iterating Over a Set

print("Question 6B:")

for number in numbers:
    print(number)


# Question 6: Adding and Removing Set Elements

numbers.add(5)

print("After adding 5:", numbers)

numbers.remove(2)

print("After removing 2:", numbers)
 
