import random
#Please Add your own words or phrase to test them out ..... here vvv
BASIC_WORDS = ["python", "testing", "hangman", "Ahnaf","Rashid","CDU","PRT582"]
#for advanced add here vvv
INTERMEDIATE_PHRASES = ["testing", "Morning Class", "software engineer", "Video Games"]

def choose_word(level: str) -> str:
    if level.lower() == "basic":
        return random.choice(BASIC_WORDS)
    if level.lower() == "intermediate":
        return random.choice(INTERMEDIATE_PHRASES)
    raise ValueError("Level not available. Use 'basic' or 'intermediate'.")
