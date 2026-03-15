def number_pattern(n):
    sequence = ''
    if type(n) != int:
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0"
    else:
        for num in range(1,n+1):
            sequence += str(num) + ' '
    return sequence.strip()

print(number_pattern(4))
