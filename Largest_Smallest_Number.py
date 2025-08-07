def largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def second_smallest(nums):
    nums = sorted(set(nums)) 
    if len(nums) < 2:
        return None  
    return nums[1]

def sec_smallest(numbers):
    sm = 0
    ssm = 0
    for i in numbers:
        if i <= sm:
            sm, ssm = i, sm
        elif i < ssm:
            ssm = i
    return ssm

      
numbers = [4, 1, 7, 3, 9, 2]
      
print(largest(numbers))
print(smallest(numbers))
print(second_smallest(numbers))
print(sec_smallest(numbers))
