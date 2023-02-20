def divisor(x):
    list_of_sum = [1]
    for i in range(2, int(x/2)+1):
        if x%i == 0:
            list_of_sum.append(i)
    return list_of_sum

set1 = set()
for i in range(1, 10000):
    x = sum(divisor(i))
    y = sum(divisor(x))
    if i == y and i!=x:
        if i not in set1:
            set1.add(i)
        if y not in set1:
            set1.add(y)
print(sum(set1))
