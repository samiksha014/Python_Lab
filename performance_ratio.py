import time

def get_performance_rate(L):
    
    def approach1(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()  # Start timing in seconds
        for i in L:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        end_time = time.time()  # End timing
        return (end_time - start_time) * 1000  # Return elapsed time in milliseconds

    def approach2(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()
        for i in L:
            if i % 2:
                odd_count += 1
            else:
                even_count += 1
        end_time = time.time()
        return (end_time - start_time) * 1000  # Return elapsed time in milliseconds

    def approach3(L):
        even_count = 0
        odd_count = 0
        start_time = time.time()
        for i in L:
            t = i % 2
            odd_count += t
            even_count += 1 - t
        end_time = time.time()
        return (end_time - start_time) * 1000  # Return elapsed time in milliseconds

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
        return (end_time - start_time) * 1000  # Return elapsed time in milliseconds

    # Measure performance for each approach
    Time1 = approach1(L)
    Time2 = approach2(L)
    Time3 = approach3(L)
    Time4 = approach4(L)

    # Calculate performance ratios
    total_time1 = Time2 + Time3 + Time4
    total_time2 = Time1 + Time3 + Time4
    total_time3 = Time1 + Time2 + Time4
    total_time4 = Time1 + Time2 + Time3

    ratios = {
        "Ratio1": ((total_time1 - Time1) / total_time1) * 100 if total_time1 > 0 else 0,
        "Ratio2": ((total_time2 - Time2) / total_time2) * 100 if total_time2 > 0 else 0,
        "Ratio3": ((total_time3 - Time3) / total_time3) * 100 if total_time3 > 0 else 0,
        "Ratio4": ((total_time4 - Time4) / total_time4) * 100 if total_time4 > 0 else 0,
    }

    max_ratio = max(ratios['Ratio1'],ratios['Ratio2'],ratios['Ratio3'],ratios['Ratio4'])
    if ratios['Ratio1'] == max_ratio:
        a = ratios['Ratio1']
        print(f"Approach 1 is {a}% faster than Approach 2, Approach 3, Approach 4.")
    elif ratios['Ratio2'] == max_ratio:
        b = ratios['Ratio2']
        print(f"Approach 2 is {b}% faster than Approach 1, Approach 3, Approach 4.")
    elif ratios['Ratio3'] == max_ratio:
        c = ratios['Ratio3']
        print(f"Approach 3 is {c}% faster than Approach 1, Approach 2, Approach 4.")
    else:
        d = ratios['Ratio4']
        print(f"Approach 4 is {d}% faster than Approach 1, Approach 2, Approach 3.")
    
    return ratios

    

# Example usage with a list of 100000 numbers as for smaller range of numbers the time it showed was zero
L = [i for i in range(1, 100000)]  # A list of numbers from 1 to 1000
print("Performance ratios ",get_performance_rate(L))
