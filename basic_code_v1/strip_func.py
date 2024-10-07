# this func can be used to systematically raser certain char at the beginning and/or at the end of a string 

text = "  Hallo, Welt!  "
print(f"Original: '{text}'")
print(f"Mit strip(): '{text.strip()}'")

text = "---Hallo, Welt!---"
print(f"Original: '{text}'")
print(f"Mit strip('-'): '{text.strip('-')}'")

text = "  Hallo, Welt!  "
print(f"Original: '{text}'")
print(f"Mit lstrip(): '{text.lstrip()}'")
print(f"Mit rstrip(): '{text.rstrip()}'")

