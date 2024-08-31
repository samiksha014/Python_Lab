
#function to get the input and convert it into required base 
def base(text, text_base, output_base):
    # Manually convert the number from the input base to decimal
    values = 0
    power = 0
    n = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in reversed(text):
        values += n.index(i.upper()) * (text_base ** power)
        power += 1
    
    # Convert the decimal value to the output base 
    if output_base == 10:
        return str(values)
    elif output_base < 36:
        return decimal(values, output_base)
    elif output_base == 36:
        return roman(values)
    else:
        return "value error"

# conversion of the input using output base
def decimal(values, base):
    n = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    if values == 0:
        return "0"
    
    while values > 0:
        result = n[values % base] + result
        values //= base
    
    return result

#conversion of input into roman as 36th testcase included in it
def roman(values):
    if not 1 <= values <= 3999:
        return "value error"

    roman_values = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100),  ('XC', 90),  ('L', 50),  ('XL', 40),
        ('X', 10),   ('IX', 9),   ('V', 5),   ('IV', 4),
        ('I', 1)
    ]
    
    result = ""
    for roman, m in roman_values:
        while values >= m:
            result += roman
            values -= m
            
    return result
    
print(base("10111",2,3))
print(base("1111",4,36))
	
