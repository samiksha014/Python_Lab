
def get_second_smallest_and_largest(lst):
    smallest = 0
    second_smallest = 0
    largest = 0
    second_largest = 0

    for item in lst:  # Iterate over each element in the input list

        # Check if the item is a list or tuple
        if type(item) == list or type(item) == tuple:
            for sub_item in item:  # Iterate over sub-items
                if type(sub_item) == int or type(sub_item) == float or type(sub_item) == complex:
                    value = sub_item.real if type(sub_item) == complex else sub_item

                    # Update smallest and second smallest
                    if smallest == 0 or value < smallest:
                        second_smallest, smallest = smallest, value
                    elif value != smallest:
                        if second_smallest == 0 or value < second_smallest:
                            second_smallest = value

                    # Update largest and second largest
                    if largest == 0 or value > largest:
                        second_largest, largest = largest, value
                    elif value != largest:
                        if second_largest is None or value > second_largest:
                            second_largest = value

        elif type(item) == int or type(item) == float or type(item) == complex:
            value = item.real if type(item) == complex else item

            # Update smallest and second smallest
            if smallest == 0 or value < smallest:
                second_smallest, smallest = smallest, value
            elif value != smallest:
                if second_smallest == 0 or value < second_smallest:
                    second_smallest = value

            # Update largest and second largest
            if largest == 0 or value > largest:
                second_largest, largest = largest, value
            elif value != largest:
                if second_largest == 0 or value > second_largest:
                    second_largest = value

    return second_smallest, second_largest


second_smallest, second_largest = get_second_smallest_and_largest( [1.3, [1.2, 3], complex(1, 4), (4, [1, 3]),"sggs", {"a": 15, "b": 7, "c": 25}])
print("Second smallest number:", second_smallest)
print("Second largest number:", second_largest)









