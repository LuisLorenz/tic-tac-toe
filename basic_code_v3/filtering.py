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
    # all letters that are in lower case 
    # what does lower() do in this case?


filtered_sentence = [char for char in sentence if is_consonant(char)]
print(filtered_sentence)