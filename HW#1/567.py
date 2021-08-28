
class Task567():
    def __init__(self, n):
        self.n = n
    
    def factorialof(self, value):
        result = 1
        for x in range(1, value + 1):
            result *= x
        return result

    def three_consecutive(self):
        listofnum = []
        for x in range(1, self.factorialof(self.n) + 1):
            listofnum.append(x)
        for i in range(len(listofnum) - 2):
            res = listofnum[i] * listofnum[i+1] * listofnum[i+2]
            if self.factorialof(self.n) == res :
                return True
        return False
