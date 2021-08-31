def simle_value(num):
    count = 0
    for x in range(1, num + 1):
        if num % x == 0:
            count += 1
    if count <= 2:
        return True
    else:
        return False

def simple_divisors(n):
    if n > 0 :
        list_values = []
        for x in range(1, n + 1):
            if n % x == 0 and simle_value(x) == True:
                list_values.append(x)

        return list_values
