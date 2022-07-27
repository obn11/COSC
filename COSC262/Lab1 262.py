def sort_of(numbers):
    """'"""
    if len(numbers) == 0:
        return []
    else:
        i = len(numbers) - 1
        output = []
        mini = numbers[-1]        
        while i >= 0:
            if numbers[i] < mini:
                mini = numbers[i]
                output.append(mini)
            else:
                output.append(mini)
            i -= 1
            print(output)
        output.reverse()
        return output
    
def concat_list(strings):
    """'"""
    if len(strings) == 0:
        return ""
    else:
        return str(strings[0]) + concat_list(strings[1:])
    
def product(data):
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])
    
def backwards(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + backwards(s[:-1]) 

def odds(data, output=0):
    if output == 0:
        output = []
    
    if data == []:
        return output
    else:
        if data[0] % 2 == 1:
            output.append(data[0])
        return odds(data[1:], output)
    
def squares(data):
    """'"""
    if data == []:
        return []
    else:
        previous = squares(data[1:])
        square = data[0]**2
        new = [square]
        return new + previous

def find(data, value, index=0):
    """'"""
    if data == []:
        return -1
    else:
        if value == data[0]:
            return index
        else:
            index += 1
            return find(data[1:], value, index)