
def get_valid_vowel(string):
    vowels = "aeiou"
    vowel_counts = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
    
    for char in string:
        if char in vowels:
            vowel_counts[char] += 1  
    
    unique_vowel_counts = []
    for count in vowel_counts.values():
        if count > 0:
            unique_vowel_counts.append(count)
    
    return len(set(unique_vowel_counts)) == 1, len(unique_vowel_counts)

def get_vowel_count(s1, s2):
    valid_s1, vowel_count_s1 = get_valid_vowel(s1)  
    valid_s2, vowel_count_s2 = get_valid_vowel(s2)  
    
    if valid_s1 and valid_s2 and vowel_count_s1 == vowel_count_s2:
        result = vowel_count_s1
    else:
        result = 0 
    
    return result


print("count:",get_vowel_count("aabeeii", "abeci"))  

