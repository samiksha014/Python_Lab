# find the count of sub string while it has overlapping or non-overlapping occurences

#first approach 
def count_fun(string,sub_string,flag):
    # num identifier will carry the count of the non overlapping sub strin
    num = 0
    
    #counts non overlapping sub strings in the given string if the flag is set to false
    if flag==False:
        i = 0
        
        while i < len(string)-1:
            if string[i] + string[i+1] == 'gg':
                num += 1
                
                #this will iterate over next to check the non-overlapping of the sub string
                i += 2
                
            else:
                # otherwise the iterator will iterate by 1
                i += 1
   
    else:   
        # for loop to avoid the string length go out of bounds 
        for i in range(len(string)-1):
           if string[i] + string[i+1] == 'gg':
                num+=1
        return num
                
print(count_fun("sgggs",'gg',True))
        
