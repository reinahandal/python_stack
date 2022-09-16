# biggie size
def biggie_size(list):
    for x in range(0,len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list
y = biggie_size([-1, 3, 5, -5])
print(y)

# count positives
def count_positives(list):
    count = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            count += 1
        if i == len(list) - 1:
            list[i] = count
    return list
x = count_positives([-1,1,5,-2,-7,6])
print(x)

# sum total
def sum_total(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum
x = sum_total([6,3,-2])
print(x)

# average
def average(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum / len(list)
x = average([1,2,3,4])
print(x)

# length
def length(list):
    return len(list)
print(length([]))

#  minimum
def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for i in range(0, len(list)):
        if list[i] < min:
            min = list[i]
    return min
x = minimum([9,-3,-6,4,3,-3])
print(x)

# maximum
def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
    return max
x = maximum([])
print(x)

# ultimate analysis
def ultimate_analysis(list):
    sum = 0
    avg = 0
    min = list[0]
    max = list[0]
    for i in range(0, len(list)):
        sum += list[i]
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]
    avg = sum / len(list)
    dictionary =  {'sumTotal': sum, 'average': avg, 'minimum': min, 'maximum': max, 'length': len(list) }
    return dictionary
x = ultimate_analysis([37,2,1,-9])
print(x)

# reverse list
def reverse_list(list):
    temp = 0
    lastvalue = round(len(list)/2)
    for i in range(0, lastvalue):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
x = reverse_list([37,1,5,6])
print(x)