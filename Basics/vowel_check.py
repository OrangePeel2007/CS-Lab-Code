word=input("enter a word: ")

if any(ch in 'aeiou' for ch in word):
    print("Vowel Found!")
else:
    print("No vowels :(")
    

