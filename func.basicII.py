def countdown(num):
    for i in range(num, -1, -1):
        print(i)
countdown(5)



def print_and_return(my_list):
    print(my_list[0])
    return my_list[1]
print(print_and_return([1,2]))



def first_plus_length(nums):
    print(nums)
    return nums[0] + len(nums)
print(first_plus_length([1,2,3,4,5]))



def values_greater_than_second(greater):
    if len(greater) < 2:
        return False
    new_list = []
    for i in greater:
        if i > greater[1]:
            new_list.append(i)
    print(len(new_list))
    return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))



def length_and_value(size, value):
    new_list2 = []
    for i in range(size):
        new_list2.append(value)
    return new_list2
print(length_and_value(4,7))
print(length_and_value(6,2))
    
    











# def greet(name, age, children):
#     print(f"Hello, my name is {name}  im {age} years old  and  kid {children}")

# greet('mohammad', '50', '12') # mohammad
# greet('bashar',  '30', '0') # bashar
# greet('emil',  '40',  '2') # emil

#TypeError: greet(x,y,z) missing 2 required positional arguments: 'y' and 'z'

#TypeError: greet() takes 0 positional arguments but 1 was given

# first_name = "nasri"
# my_age = 72
# children = 12

# print(f"Hello, my name is {first_name} i am {my_age} years old i have {children} kids")

