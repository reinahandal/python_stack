# COUNTDOWN
empty_list = []
def countdown(num):
    for i in range(num, -1, -1):
        empty_list.append(i)
    return empty_list
print(countdown(8))

# PRINT AND RETURN
def print_and_return(empty_list):
    print(empty_list[0])
    return empty_list[1]
y = print_and_return([3,5])
print(y)

# FIRST PLUS LENGTH
def first_plus_length(list):
    return list[0] + len(list)
z = first_plus_length([1,2,3,4,5])
print(z)

# VALUES GREATER THAN SECOND
def values_greater_than_second(list):
    newlist =[]
    for i in range(0, len(list)):
        if len(list) < 2:
            return False
            break
        elif list[i] > list[1]:
            newlist.append(list[i])
    print(len(newlist))
    return newlist
y = values_greater_than_second([5,2,3,2,1,4])
print(y)

# THIS LENGTH, THAT VALUE
def length_and_value(size,value):
    list = []
    for i in range(0,size):
        list.append(value)
    return list
x = length_and_value(4,7)
print(x)