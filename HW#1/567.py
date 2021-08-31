def factorialof(value):
    result = 1
    for x in range(1, value + 1):
        result *= x
    return result

def three_consecutive(n):
    listofnum = []
    for x in range(1, factorialof(n) + 1):
        listofnum.append(x)
    for i in range(len(listofnum) - 2):
        res = listofnum[i] * listofnum[i+1] * listofnum[i+2]
        if factorialof(n) == res :
            return True
    return False
