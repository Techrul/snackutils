#== Import Stuff ==
import random
import sys

#== State functions ==
__all__ = ["eight_ball", "flip_coin", "roll_dice", "detect_os", "average", "mean", "average_list", "mean_list"]

#== Functions ==

_ANSWERS = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

def eight_ball() -> str:
    return random.choice(_ANSWERS)

# --------------------------------------------------------------------------

def flip_coin() -> str:
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    else:
        return "Tails"

# --------------------------------------------------------------------------

def roll_dice() -> int:
    return random.randint(1,6)

# --------------------------------------------------------------------------

def detect_os() -> str: #I made this as readable as possible in my opinion
    name = sys.platform
    if name == "win32":
        return "Windows"
    elif name == "darwin":
        return "MacOS"
    elif name == "ios":
        return "iOS"
    else:
        return name.title()

# --------------------------------------------------------------------------

def average(num1: float, num2: float) -> float:
    return sum([num1, num2]) / 2

mean = average

# --------------------------------------------------------------------------

def average_list(numbers: list[float]) -> float:
    return sum(numbers) / len(list)

mean_list = average_list