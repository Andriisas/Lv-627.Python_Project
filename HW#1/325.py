class Task325():
    def __init__(self, n):
        self.n = n

    def simle_value(self, num):
        count = 0
        for x in range(1, num + 1):
            if num % x == 0:
                count += 1
        if count <= 2:
            return True
        else:
            return False

    def simple_divisors(self):
        if self.n > 0 :
            list_values = []
            for x in range(1, self.n + 1):
                if self.n % x == 0 and self.simle_value(x) == True:
                    list_values.append(x)

            return list_values
