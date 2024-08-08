# find the count of sub string while it has overlapping or non-overlapping occurences

#first approach 
def count_fun(string,sub_string,flag):
    
    #counts non overlapping sub strings in the given string if the flag is set to false
    if flag==False:
        # c identifier will carry the count of the non overlapping sub string
        c = string.count('gg')
        return c
        
    else:
        # the count of the sub strings 
        num = 0
        
        # for loop to avoid the string length go out of bounds 
        for i in range(len(string)-1):
           if string[i] + string[i+1] == 'gg':
                num+=1
        return num
                
print(count_fun("sgggs",'gg',True))
        
