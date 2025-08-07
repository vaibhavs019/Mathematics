def sum_of_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

def sum_even_pos(numbers):
    sum_of_even = 0
    for i in numbers:
        if i%2 == 0:
            sum_of_even = sum_of_even + i
    return sum_of_even

def sum_odd_pos(numbers):
    sum_of_odd = 0
    for i in numbers:
        if i%2 != 0:
            sum_of_odd = sum_of_odd + i
    return sum_of_odd

def sum_odd(numbers):
    sum_odd = 0
    for num in numbers:
        if num%2 != 0:
            sum_odd += num
    return sum_odd

def sum_even(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even



numbers = [2,1,4,3,5]

print(sum_odd_pos(numbers))
print(sum_even_pos(numbers))
print(sum_of_list(numbers))
print(sum_odd(numbers))
print(sum_even(numbers))