# Quiz 

from colorama import Fore, Style

class Quiz():
    def __init__(self, score = 0):
        
        self.score = score
        self.Menu()

    def Menu(self):

        print(Fore.RED + "\n--- W E L C O M E ---")
        print(Fore.BLUE + "\nLevels:")
        print(Fore.GREEN + "\n1. Easy\n2. Medium\n3. Hard")

        while True:

            level = input(Fore.YELLOW + "\nPlease select the difficulty level: " + Style.RESET_ALL + "").lower()

            if level in ["1", "one", "easy"]:

                self.Easy()
                self.DisplayQuiz(self.easy_questions)

            elif level in ["2", "two", "medium"]:

                self.Medium()
                self.DisplayQuiz(self.medium_questions)

            elif level in ["3", "three", "hard"]:

                self.Hard()
                self.DisplayQuiz(self.hard_questions)

            else:
                print(Fore.RED + "\nInvalid Option!")
                continue

    def DisplayQuiz(self, questions):
        
        for q in questions:
            print(Fore.CYAN + f"\nQuestion: {q['Question']}\n")
            for key, value in q["Options"].items():
                print(f"{key}. {value}")

            answer = input(Fore.RED + "\nAnswer: " + Style.RESET_ALL + "").strip().lower()

            correct_key = q["Answer"].lower()
            correct_text = q["Options"] [q["Answer"]].strip().lower()

            if answer in [correct_key, correct_text]:
                print(Fore.GREEN + "\nCorrect!")
                self.score += 1

            else:
                print(Fore.MAGENTA + f"\nWrong! The correct answer was {q['Answer']}.")

        print(Fore.CYAN + f"\nScore: {self.score}/{len(questions)}")

        while True:

            yes_or_no = input(Fore.GREEN + "\nDo you want to continue? (Y / N): " + Style.RESET_ALL + "").upper()

            if yes_or_no in ["Y", "YES"]:
                self.Menu()

            elif yes_or_no in ["N", "NO"]:
                quit()

            else:
                print(Fore.RED + "\nInvalid option!")
                continue

    def Easy(self):
        
       self.easy_questions = [
        {
            "Question": "Which planet is known as the Red Planet?",
            "Options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
            "Answer": "B"
        },
        {
            "Question": "What is the largest mammal in the world?",
            "Options": {"A": "Elephant", "B": "Blue Whale", "C": "Giraffe", "D": "Hippopotamus"},
            "Answer": "B"
        },
        {
            "Question": "Which element has the chemical symbol 'O'?",
            "Options": {"A": "Gold", "B": "Oxygen", "C": "Iron", "D": "Silver"},
            "Answer": "B"
        },
        {
            "Question": "What is the square root of 64?",
            "Options": {"A": "6", "B": "8", "C": "7", "D": "9"},
            "Answer": "B"
        },
        {
            "Question": "Which country is famous for the Great Wall?",
            "Options": {"A": "China", "B": "Italy", "C": "Egypt", "D": "Mexico"},
            "Answer": "A"
        }
        ]

    def Medium(self):
        
        self.medium_questions = [
        {
            "Question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
            "Options": {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Nitrogen", "D": "Hydrogen"},
            "Answer": "B"
        },
        {
            "Question": "Who wrote the play Romeo and Juliet?",
            "Options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Jane Austen", "D": "Mark Twain"},
            "Answer": "B"
        },
        {
            "Question": "What is the smallest prime number greater than 10?",
            "Options": {"A": "11", "B": "12", "C": "13", "D": "14"},
            "Answer": "A"
        },
        {
            "Question": "Which organ in the human body is primarily responsible for detoxification?",
            "Options": {"A": "Heart", "B": "Liver", "C": "Kidney", "D": "Lungs"},
            "Answer": "B"
        },
        {
            "Question": "In computing, what does 'CPU' stand for?",
            "Options": {"A": "Central Processing Unit", "B": "Computer Primary Unit", "C": "Central Programming Unit", "D": "Control Processing Unit"},
            "Answer": "A"
        }
        ]

    def Hard(self):
        
        self.hard_questions = [
        {
            "Question": "What is the derivative of sin(x) with respect to x?",
            "Options": {"A": "cos(x)", "B": "-cos(x)", "C": "sin(x)", "D": "-sin(x)"},
            "Answer": "A"
        },
        {
            "Question": "Which element has the highest melting point?",
            "Options": {"A": "Iron", "B": "Tungsten", "C": "Carbon", "D": "Osmium"},
            "Answer": "B"
        },
        {
            "Question": "Which planet has the shortest day in the solar system?",
            "Options": {"A": "Jupiter", "B": "Mars", "C": "Venus", "D": "Mercury"},
            "Answer": "A"
        },
        {
            "Question": "Which mathematician is known for the theory of relativity?",
            "Options": {"A": "Isaac Newton", "B": "Albert Einstein", "C": "Galileo Galilei", "D": "Nikola Tesla"},
            "Answer": "B"
        },
        {
            "Question": "Which country has the highest number of volcanoes?",
            "Options": {"A": "Indonesia", "B": "Japan", "C": "Italy", "D": "United States"},
            "Answer": "A"
        }
        ]

Quiz()

