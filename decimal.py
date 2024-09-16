

def decimal_subtraction(n1 , n2):

    decimal_dict = { "0":0 ,"1":1 ,"2":2 ,"3":3, "4":4, "5":5 , "6":6 ,"7":7 ,"8":8 ,"9":9}
    subtract = 0

    def str_to_int(text):
        r = 0
  
        if len(text) == 0:
            return 0
        elif len(text) == 1:
            return decimal_dict[text]
    
        else:
            for i,j in enumerate(text[::-1]):
                if j in decimal_dict:
                    r += decimal_dict[j]*(10**i)
            return r
        
    num1 = str_to_int(n1)
    num2 = str_to_int(n2)
    
    subtract = num1 - num2
    return subtract
    
    
        
print("subtraction of n1 and n2 : ",decimal_subtraction("1","2"))
print("subtraction of n1 and n2 : ",decimal_subtraction("10","7"))
        

            
        
    
