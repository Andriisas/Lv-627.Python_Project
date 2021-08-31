def firstdigit(value):
    if value > 0:
        string_value = str(value)
        list_values = []
        for x in string_value:
            list_values.append(int(x))
        return list_values[0]
    else:
        return 'Enter Natural number!'
        
