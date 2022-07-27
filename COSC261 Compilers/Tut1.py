def all_strings(alpha, length):
    """'"""
    if length == 0:
        return [""]
    else:
        output = []
        last_answer = all_strings(alpha, length-1)
        for string in last_answer:
            for letter in alpha:
                temp = string
                temp += str(letter)
                output.append(temp)
        return output