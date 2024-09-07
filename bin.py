
#result variable will store the overall subtraction of the given numbers
result = 0
# to handle borrow in the subtraction
b = 0

#function created to subtract the given numbers and return the result
def binary_subtraction(num1,num2):
    
    num1 = int(num1,2)
    num2 = int(num2,2)
    
    while num2 != 0:
    #borrow to determine the borrow position
        b = (~num2) & num2
    #XOR performs initial subtraction 
        num1 = num1 ^ num2
        num2 = b << 1
        num1 = bin(num1)[2:]
    return num1
    
print("binary subtraction of given binary numbers is :- ",binary_subtraction("100","110"))
	
