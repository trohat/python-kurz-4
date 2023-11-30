import re

# Zadání věty do proměnné
vetou_o_slovech = "Toto je příklad věty obsahující několik slov."

# a) Změna všech písmen na velká
velka_veta = vetou_o_slovech.upper()
print("Věta s velkými písmeny:", velka_veta)

# b) Změna všech písmen na malá
mala_veta = vetou_o_slovech.lower()
print("Věta s malými písmeny:", mala_veta)

# c) První písmeno ve větě velké
prvni_velke = vetou_o_slovech.capitalize()
print("První písmeno ve větě velké:", prvni_velke)

# d) První písmeno každého slova ve větě velké
vsechna_velka = vetou_o_slovech.title()
print("První písmeno každého slova ve větě velké:", vsechna_velka)

# e) Udělejte ze stringu seznam, tak aby každá položka seznamu bylo jedno slovo
seznam = list(vetou_o_slovech)
print("e) Seznam písmen ze věty:", seznam)

seznam_slov = vetou_o_slovech.split()
print(seznam_slov)

# f) Udělejte ze seznamu opět string s pomlčkami místo mezer
retezec_s_pomlckami = "-".join(seznam_slov)
print("f) Řetězec s pomlčkami místo mezer:", retezec_s_pomlckami)

#===========================================
# JELENOVIPIVONELEJ
#Jelenovi pivo nelej
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# User input
user_string = input("Enter a string: ")

# Check if it's a palindrome
if is_palindrome(user_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#==============================================


def modify_reserved_words(text, reserved_words):
    words = text.split()

    # Iterate through the words
    modified_words = [word.upper() if word.lower() in reserved_words else word for word in words]

    modified_text = ' '.join(modified_words)
    return modified_text

# Reserved words
reserved_words = ["python", "reserved", "words", "example"]

# User input
user_text = input("Enter text: ")

# Modify the text
modified_text = modify_reserved_words(user_text, reserved_words)

print("Modified Text:")
print(modified_text)

 #===================================


def count_sentences(text):
    sentences = [sentence.strip() for sentence in re.split(r'[.!?]', text) if sentence.strip()]

    return len(sentences)

# User input
user_text = input("Enter some text: ")

num_sentences = count_sentences(user_text)

# Print the result
print(f"Number of sentences: {num_sentences}")

#========================================


def evaluate_arithmetic_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

# User input
user_expression = input("Enter an arithmetic expression (e.g., 23+12): ")

# Evaluate the expression
result = evaluate_arithmetic_expression(user_expression)

# Print the result
if result is not None:
    print(f"Result: {result}")

#====================================