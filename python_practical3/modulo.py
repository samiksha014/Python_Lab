#numerator = dividend
#denominator = divisor

def modulo(numerator,denominator):
    if denominator == 0:
        return "Undefined Operation"

    
    #to get acurate floating point resukt we use float division here
    result = numerator // denominator
    if result >= 0:
        var = int(result)
    else:
        var = int(result) - 1
    mod = numerator - (var * denominator)
    return mod

num = float(input())
deno = float(input())
print(modulo(num,deno))

