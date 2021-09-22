"""Write a program to accept a number from a user and calculate the sum of
all numbers from 1 to a given number
For example, if the user entered 10 the output should be 55
(1+2+3+4+5+6+7+8+9+10)
Enter number 10
Sum is: 55"""


def add_num():
    num = int(input("Enter your value: "))
    sum = 0
    for i in range(1, num+1, 1):
        sum = sum + i
    return sum

#print(add_num())

"""Write a program to print multiplication table of a given number"""

def multiplication():
    num = int(input("Enter num for its multiplication: "))
    #ran = int(input("Enter range for multiplication: "))
    for i in range(1, 11):
        print(num * i)

#print(multiplication())


"""Write a program to display only those numbers from a list that satisfy
the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next
number
If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
75
150
145
4. Print list in reverse order"""


def display_num():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for i in numbers:
        if i > 500:
            break
        elif i > 150 & i % 5 == 0:
            continue
        elif i % 5 == 0:
            print(i)



#print(display_num())


"""Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
50
40
30
20
10"""


def print_reverse():
    list1 = [10, 20, 30, 40, 50]
    print(list1[::-1])

def print_reverse1():
    list1 = [10, 20, 30, 40, 50]
    print(list1[::-1])

#print_reverse()


"""Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
20 40 60 80 100"""


def display_ele():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in range(0, len(my_list)):
        if not i % 2 == 0:
            print(my_list[i])

#display_ele()


"""Return a new set of identical items from a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
{40, 50, 30}"""


def iden_set():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    print("Identical Set ")
    print(set1 & set2)

    print("Non Identical Set ")
    print(set1 | set2)

    print("Diff Set ")
    print(set1 & set2)

#iden_set()

"""Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
{70, 40, 10, 50, 20, 60, 30}"""

def remove_dup():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1 | set2)

#remove_dup()


"""Given two Python sets, update the first set with items that exist only in the first set and not in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1 {10, 30}"""

def remove_dup1():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    print(set1 - set2)

#remove_dup1()

"""Return a set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
{20, 70, 10, 60}"""


def ret_set():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1 - set2 | set2 - set1)

#ret_set()