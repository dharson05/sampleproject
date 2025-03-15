import random

def shuffle_word(word):
    return "".join(random.sample(word, len(word)))

def word_puzzle():
    words = ["python", "developer", "puzzle", "challenge", "program"]
    word = random.choice(words)
    scrambled = shuffle_word(word)
    
    print("Word Puzzle: Unscramble the letters to form a word!")
    print("Scrambled word:", scrambled)
    
    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ")
        if guess.lower() == word:
            print("Congratulations! You got it right.")
            return
        else:
            attempts -= 1
            print(f"Incorrect! {attempts} attempts left.")
    
    print(f"Sorry, the correct word was '{word}'. Try again!")

if __name__ == "__main__":
    word_puzzle()
