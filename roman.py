
# integer to roman representation of the given value

def roman(text, text_base):

    # converting string input to integer with its base 
    text = int(text, text_base)
    
    # reference variable for integer to roman conversion
    integer_to_roman = ''
    
    # list containing tuple with integers and its roman values 
    values = [ (1000,'M') , (900, 'CM') , (500, 'D') , (400, 'CD') , (100, 'C'),
                (90,'XC') , (50,'L') , (40,'XL') , (10,'X') , (9, 'IX') , (5, 'V'),
                (4,'IV'), (1,'I') 
            ]
    #for loop to add the required roman value of the text integer given         
    for (integer_value, roman_value) in values:
        if text >= integer_value:
            integer_to_roman += roman_value
            #here if the preceding value is greater than the current it gets minus for getting the required value
            text -= integer_value
    return integer_to_roman

print("Integer to roman conversion:- ", rom("1000",8))
    
    
    

