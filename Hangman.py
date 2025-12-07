# Welcome to Hangman!

import random

print('''

--------------------------------------------
--------------------------------------------
               H A N G M A N                
--------------------------------------------
--------------------------------------------

''')


print("Difficulty Levels:\n")
print("1. Easy")
print("2. Medium")
print("3. Hard")         
print("4. Quit (Q / 4)")

# 100 words for each difficulty level

easy_words = [
    "apple", "house", "chair", "bread", "table", "grape", "plant", "smile", "cloud", "river", "ocean", "sleep", "drink", "grass", "sheep", "stone", "lemon", "honey", "tiger", "sunny",
    "happy", "green", "light", "heart", "dream", "water", "music", "laugh", "sweet", "world", "phone", "pizza", "mango", "berry", "sugar", "pasta", "shirt", "pants", "white", "black",
    "brown", "train", "truck", "beach", "flame", "dance", "grill", "candy", "toast", "smoke", "spark", "clock", "spoon", "couch", "radio", "piano", "brush", "broom", "socks", "boots",
    "zesty", "towel", "purse", "knife", "forks", "plate", "bacon", "noisy", "tummy", "funny", "cabin", "maple", "pearl", "frost", "storm", "shift", "crisp", "melon", "cheer", "smile",
    "globe", "crown", "paper", "pencil", "marker", "index", "magic", "scoop", "honey", "tight", "outer", "inner", "shine", "shadow", "blend", "fresh", "glass", "metal"
]

medium_words = [
    "library", "blanket", "kitchen", "village", "harvest", "lantern", "battery", "station", "compass", "freedom", "journey", "captain", "dentist", "railway", "volcano", "tornado",
    "thunder", "factory", "diamond", "ancient", "balcony", "circus", "crystal", "fortune", "gravity", "kingdom", "picture", "puzzle", "rocket", "scholar", "statue", "temple",
    "theater", "whisper", "horizon", "mission", "cottage", "perfume", "spinach", "almond", "orange", "bottle", "canyon", "festival", "vintage", "storage", "popcorn", "brother",
    "shelter", "context", "teacher", "student", "program", "account", "orchard", "forward", "capture", "balance", "collect", "counter", "fiction", "gallery", "gateway", "holiday",
    "history", "freight", "journal", "justice", "measure", "mindset", "notebook", "passage", "pattern", "percent", "perform", "plastic", "profile", "railroad", "science", "sunrise",
    "texture", "timber", "treason", "venture", "veteran", "weather", "woodland", "writing", "charter", "compute", "develop", "enhance", "storage", "upgrade", "exhibit", "adviser","content", "decoder", "message"
]

hard_words = [
    "labyrinth", "chrysanthemum", "kaleidoscope", "metamorphosis", "inconceivable", "unobtainable", "iridescence", "juxtaposition", "reconnaissance", "transcendence",
    "connoisseur", "acquiescence", "idiosyncratic", "quintessential", "photosynthesis", "anthropomorphic", "discombobulate", "hyperbolic", "dichotomy", "phantasmagoria",
    "onomatopoeia", "soliloquy", "pseudonym", "euphemism", "epiphany", "nebulous", "cacophony", "clandestine", "harmonious", "magnanimous", "vehemently", "serendipity",
    "oscillation", "equilibrium", "ambidextrous", "pernicious", "obstreperous", "aristocracy", "plebiscite", "jurisprudence", "archipelago", "bougainvillea",
    "mesmerization", "transmogrify", "uncharacteristic", "superfluous", "idolatrous", "perspicacity", "vociferous", "multifarious", "ineffable", "belligerent",
    "circumference", "disenfranchise", "ethereal", "fortuitous", "grandiloquent", "heterogeneous", "imperceptible", "intransigent", "lugubrious", "mellifluous",
    "nonchalant", "obfuscation", "parsimonious", "preposterous", "quizzical", "recrimination", "sagacious", "tantamount", "ulterior", "vocational",
    "whimsical", "xenophobia", "yesteryear", "zealousness", "apostrophe", "benefactor", "camaraderie", "deleterious", "ellipsoid", "fastidious",
    "garrulous", "hallucination", "illumination", "juxtaposed", "kinesthetic","lexicology", "misogynistic", "nihilistic", "onomastic", "paradoxical", "quarantine", "retroactive", "synchronous", "trigonometry", "voracious"
]

# Hangman Stages

hangman_stages = [

    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


while True:

    difficulty_level = input("\nPlease select the difficulty level (1-3), or Quit (Q / 4): ").lower()

    if difficulty_level in ["1", "easy"]:
        print("\nDifficulty level selected: 'Easy.'")
        word = random.choice(easy_words)
        break


    elif difficulty_level in ["2", "medium"]:
        print("\nDifficulty level selected: 'Medium.'")
        word = random.choice(medium_words)
        break


    elif difficulty_level in ["3", "hard"]:
        print("\nDifficulty level selected: 'Hard.'")
        word = random.choice(hard_words)
        break

    elif difficulty_level in ["q", "quit", "4"]:
        print("\nThanks for using my program!\n")
        quit()

    else:
        print("\nPlease enter a valid option!")

def Game(word):
    word = word.upper()
    max_attempts = len(hangman_stages) - 1
    wrong_guesses = 0
    guessed_letters = []

    display = ["_"] * len(word)

    while wrong_guesses < max_attempts and "_" in display:
        print("\n" + "-" * 50)
        print(hangman_stages[wrong_guesses])
        print("\nWord:", " ".join(display))
        print("\nGuessed Letters:", ", ".join(guessed_letters))

        guess = input("\nGuess a letter: ").upper()
        print("\n" + "-" * 50)

        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a single letter!")
            continue

        if guess in guessed_letters:
            print("\nYou already guesses that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"\nCorrect! The letter '{guess}' is in the word.")

            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess

        else:
            print(f"\nWrong! The letter '{guess}' is not in the word.")
            wrong_guesses += 1

    if "_" not in display:
        print(f"\nWell Done! You guesses the word '{word}'.\n")
    else:
        print(hangman_stages[wrong_guesses])
        print(f"\nYou lost! The word was: {word}.\n")
        quit()

Game(word)

