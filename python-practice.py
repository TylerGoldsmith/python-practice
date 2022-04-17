# 1: Write a Python function called max_num()to find the Max of three numbers.

def max_num(a,b,c):
    return max([a,b,c])

print('Question #1: Write a function called max_num()to find the Max of three numbers')
print(max_num(1,2,3))
print(max_num(12,15,4))

# Write a Python function called mult_list()  to multiply all the numbers in a list.

def mult_list(list_1):
    if len(list_1) == 0:
        return 0
    prod = list_1[0]
    if len(list_1) > 1:
        for i in list_1[1:]:
            prod = prod * i
            return prod
print('Question #2: Write a function called mult_list() to multiply all the numbers in a list')    
print(mult_list([1,2]))
print(mult_list([10,10]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[::-1]

print('Question #3: Write a Python function called rev_string() to reverse a string.')
print(rev_string("Hello World"))
print(rev_string("smile"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
    return x in range(a,b+1)
     
print('Question #4: Write a Python function called num_within() to check whether a number falls')     
print(num_within(2,1,3))     
print(num_within(20,5,12))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
    if n < 1:
        print("Not enough rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
        for i in range(length):
            if i == 0:
                row.append(1)
            elif i > 0 and i < length-1:
                row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
            else:
                row.append(1)
                triangle.append(row)
                row_number += 1

    #print triangle
    for row in triangle:
      print(row)

print("Question #5: Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.")
pascal(2)
pascal(5)