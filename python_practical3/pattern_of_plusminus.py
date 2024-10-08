#pattern printing 


#function to take the input as the length and then print the required pattern

def pattern_printing(length):
    if length<1:
        return "the given length is not valid , enter the number greater than equal to 1"
        
    else:
        #empty string to store the pattern
        pattern=[]
        
        #iteration of each row
        for i in range(length * 3):
            line=[]
            
            #iteration of each column according to print the specified pattern
            for j in range ( length * 2 + 3 ):
                    
                if i <= length and j <= length + 1:
                    if i + j == length+1:
                        line.append("+")
                    else:
                        line.append(" ")
                        
                elif i>length and j<=length+1 and i<=length*2-1:
                    if i-j == length-1:
                        line.append("+")
                    else:
                        line.append(" ")
                        
                elif i<= length and j>length+1:
                    if j-i == length+1:
                        line.append("+")
                    else:
                        line.append(" ")
                        
                elif i>length and j>length+1 and i<=length*2-1:
                    if i+j == length*3+1:
                        line.append("+")
                    else:
                        line.append(" ")
                elif i>length and j>length+1:
                    if i+j == length*3+2:
                        l = length+1
                        line.append(" "*l)
                        line.append("-")
                    else:
                        line.append("")
                        
            pattern.append("".join(line))
        
        return "\n".join(pattern)
        
print(pattern_printing(3))
