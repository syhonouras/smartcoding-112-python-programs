ch = input("Enter a character: ").lower()

if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print(f"'{ch}' is a vowel.")
    else:
        print(f"'{ch}' is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic letter.")