
# change case of the given string without using change case built in functions in python , given different styles

def change_case(str,style):

    #lower_case string is provided to change the given string to lower_case 
    lower_case = "abcdefghijklmnopqrstuvwxyz"

    #upper_case string is provided to change the given string to upper_case
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = str
    
    #here in this particular logic replace method in used to replace a particular from its initial to given style 
    if style == 'c':
        for i in range(len(lower_case)):
            result = result.replace(lower_case[i], upper_case[i])
    elif style == 's':
        for i in range(len(upper_case)):
            result = result.replace(upper_case[i], lower_case[i])
    elif style == 'r':
        for i in range(len(lower_case)):
            result = result.replace(lower_case[i], upper_case[i])
            result = result.replace(upper_case[i], lower_case[i])
    elif style == 'u':
        new_result = ""
        for i, ch in enumerate(result):
            if ch in lower_case:
                if i % 2 == 0:
                    new_result += upper_case[lower_case.index(ch)]
                else:
                    new_result += ch
            elif ch in upper_case:
                if i % 2 == 0:
                    new_result += ch
                else:
                    new_result += lower_case[upper_case.index(ch)]
            else:
                new_result += ch
        result = new_result
    return result

print("from initial string to uppercase :- ",change_case("hello",'c'))
print("from initial string to lowercase :- ",change_case("Hello",'s'))
print("from initial string to its reverse :- ",change_case("Hello World",'r'))
print("from initial string to lowercase to uppercase and upper_case to lowercase (zig-zag) :- ",change_case("hello world",'u'))