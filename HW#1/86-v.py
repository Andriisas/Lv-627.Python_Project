class Task86V():
    def __init__(self,value):
        self.value = value
        
    def firstdigit(self):
        if self.value > 0:
            string_value = str(self.value)
            list_values = []
            for x in string_value:
                list_values.append(int(x))
            return list_values[0]
        else:
            return 'Enter Natural number!'