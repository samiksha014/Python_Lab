

def get_palindrome_count(L):
    palindrome = " "
    count = 0
    reg_no = 3  
    
    for obj in L:
        if type(obj) == str:
            if len(obj) % 5 == reg_no:
            
                #gives a palindrome string 
                palindrome = obj[::-1]   
                if palindrome == obj:
                    count += 1
        elif type(obj) == int:
            obj = str(obj)
            if len(obj) % 5 == reg_no:
                palindrome = obj[::-1]
                if palindrome == obj:
                    count += 1
        else:
            continue
    return count 
    
print("count:",get_palindrome_count([131,"abcddcba",(12,19)]))

