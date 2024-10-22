# adding conditional to a list comprehension
# new_list = [expression for member in iterable if conditional]

sentence = "the rocket came back from mars"
filtered_sentence = [char for char in sentence if char in "aeiou"]
print(filtered_sentence) 
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

# separating argument
sentence = (
     "The rocket, who was named Ted, came back "
     "from Mars because he missed his friends."
 )
def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels
    # first check: is letter in alphabet? 
    # second check: the letter is lowered and not in vowels?
    # returne True or False

filtered_sentence = [char for char in sentence if is_consonant(char)]
print(filtered_sentence)
# ['T', 'h', ...  's'] 'T' is in capital like it should be 

# list variations
# conditional at the beginning
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
filtered_list = [price if price > 0 else 0 for price in original_prices]
print(filtered_list)
# [1.25, 0, 10.22, 3.78, 0, 1.16]

# easier in two steps
def get_price(price):
    return price if price > 0 else 0
filtered_list = [get_price(price) for price in original_prices]
print(filtered_list)