def biggie_size(type_list):
    for i in range(len(type_list)):
        type_list[i]
        if type_list[i] > 0:
            type_list[i] = "big"
    return type_list
print(biggie_size([-1, 3, 5, -5])) 



def count_positive(write_list):
    var = 0
    for i in write_list:
        if i > 0:
            var += 1 
            write_list[len(write_list) -1] = var
    return write_list
print(count_positive([-1,1,1,1]))



def sum_total(calc):
    total = 0
    for i in calc:
        total += i
    return total
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))



def average(calc2):
    average_total = 0
    for i in calc2:
        average_total += i
    return average_total / len(calc2)
print(average([1,2,3,4]))



def length(meter_list):
    return len(meter_list)
print(length([37,2,1,-9]))
print(length([]))



def minimum(write_list2):
    if len(write_list2) <= 0:
        return False 
    smallest = write_list2[0]
    for i in write_list2:
        if i < smallest:
            smallest = i
    return smallest 
print(minimum([37, 2, 1, -9]))



def maximum(write_list3):
    if len(write_list3) <= 0:
         return False
    biggest = write_list3[0]
    for i in write_list3:
         if i > biggest:
              biggest = i
    return biggest
print(maximum([37,2,1,-9]))


def ultimate_analysis(write_list):
    result = { 
"sumTotal": sum_total(write_list),
"average": average(write_list),
"minimum": minimum(write_list),
"maximum": maximum(write_list),
"length": length(write_list)
    }

    return result

print(ultimate_analysis([37,2,1,-9]))



def reverse_list(type_list):
    for i in range(len(type_list) // 2):
        temp = type_list[i]
        type_list[i] = type_list[len(type_list) - i - 1]
        type_list[len(type_list) - i - 1] = temp
        return type_list
print(reverse_list([37,2,1,-9]))