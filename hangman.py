from dataclasses import dataclass, field
from typing import Set
HIDDEN_CHAR = "_"

@dataclass
class HangmanState:
    answer: str
    lives: int = 6
    guessed: Set[str] = field(default_factory=set)
    wrong: Set[str] = field(default_factory=set)

    def masked(self) -> str:
        out = []
        for ch in self.answer:
            if ch == " ":
                out.append(" ")  
            elif ch.lower() in self.guessed:
                out.append(ch)
            else:
                out.append(HIDDEN_CHAR)
        return "".join(out)

    def is_won(self) -> bool:
        return all(c.lower() in self.guessed or c == " " for c in self.answer)

    def is_lost(self) -> bool:
        return self.lives <= 0 and not self.is_won()

class HangmanEngine:
    def __init__(self, answer: str, lives: int = 6) -> None:
        self.state = HangmanState(answer.lower(), lives)

    def guess(self, letter: str) -> bool:
        """Return True if guess correct, else False (and deduct life)."""
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Guess must be a single letter.")

        ltr = letter.lower()
        if ltr in self.state.guessed or ltr in self.state.wrong:
            return ltr in self.state.answer  # can repeat an already given word , no penalties made

        if ltr in self.state.answer:
            self.state.guessed.add(ltr)
            return True
        else:
            self.state.wrong.add(ltr)
            self.state.lives -= 1
            return False
