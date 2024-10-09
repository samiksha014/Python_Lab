

import time

def get_performance_rate(L):

    def approach1(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()
        for i in L:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        end_time = time.time()

        #return time in milliseconds for calculating accurate performance rate
        return (end_time - start_time)*1000 

    def approach2(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()
        for i in L:
            if i % 2:
                even_count += 1
            else:
                odd_count += 1
        end_time = time.time()

        #return time in milliseconds for calculating accurate performance rate
        return (end_time - start_time)*1000 

    def approach3(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()
        for i in L:
            t = i % 2
            odd_count += t
            even_count += t
        end_time = time.time()

        #return time in milliseconds for calculating accurate performance rate
        return (end_time - start_time)*1000

    def approach4(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()
        for i in L:
            if i & 1:
                odd_count += 1
            else:
                even_count += 1
        end_time = time.time()

        #return time in milliseconds for calculating accurate performance rate
        return (end_time - start_time)*1000


    Time1 = approach1(L)
    Time2 = approach2(L)
    Time3 = approach3(L)
    Time4 = approach4(L)

    # to calculate performance rate

    total_time1 = Time2 + Time3 + Time4
    total_time2 = Time1 + Time3 + Time4
    total_time3 = Time1 + Time2 + Time4
    total_time4 = Time1 + Time2 + Time3 

    ratios = {
        "Ratio1": ((total_time1 - Time1) / total_time1) * 100 ,
        "Ratio2": ((total_time2 - Time2) / total_time2) * 100 ,
        "Ratio3": ((total_time3 - Time3) / total_time3) * 100 ,
        "Ratio4": ((total_time4 - Time4) / total_time4) * 100 ,
    }

    # getting maximum performance rate
    max_ratio = max(ratios['Ratio1'],ratios['Ratio2'],ratios['Ratio3'],ratios['Ratio4'])
    if ratios['Ratio1'] == max_ratio:
        a = ratios['Ratio1']
        print(f"Approach 1 is {a}% faster than Approach 2, Approach 3, Approach 4")
    elif ratios['Ratio2'] == max_ratio:
        b = ratios['Ratio2']
        print(f"Approach 2 is {b}% faster than Approach 1, Approach 3, Approach 4")
    elif ratios['Ratio3'] == max_ratio:
        c = ratios['Ratio3']
        print(f"Approach 3 is {c}% faster than Approach 1, Approach 2, Approach 4")
    else:
        d = ratios['Ratio4']
        print(f"Approach 1 is {d}% faster than Approach 1, Approach 2, Approach 3")

    return ratios


#Example usage with list of 100000 numbers to handle to calculate the accurate performance rate
L = [ i for i in range(1,100000)]
print("Performance ratios",get_performance_rate(L))
