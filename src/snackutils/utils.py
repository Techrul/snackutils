#== Import Stuff ==
import random
import sys
import time

#== State functions ==
__all__ = ["eight_ball", "flip_coin", "roll_dice", "detect_os", "average", "mean", "average_list", "mean_list","percent_choose", "better_sleep", "ai_detector"]

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

def detect_os() -> str: # I made this as readable as possible in my opinion
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
    return sum(numbers) / len(numbers)

mean_list = average_list

# --------------------------------------------------------------------------

def percent_choose(a: float, b: float) -> int:# a and b are percentages for options 1 and 2; each is rounded to the

    a_tenths = round(a * 10)                  # nearest tenth, must be between 0 and 100, and must add to 100.
    b_tenths = round(b * 10)

    if not (0 <= a_tenths <= 1000 and 0 <= b_tenths <= 1000):
        raise ValueError("Percentages must be between 0 and 100")
    if a_tenths + b_tenths != 1000:
        raise ValueError("Percentages must add to exactly 100")

    if random.randrange(1000) < a_tenths:
        return 1
    else:
        return 2
    
# --------------------------------------------------------------------------

_UNITS = {"second": 1, "minute": 60, "hour": 3600, "day": 86400}

def better_sleep(value: float, units: str = "seconds") -> None:
    unit = units.lower().removesuffix("s")
    if unit not in _UNITS:
        raise ValueError(f"Unknown unit: {units!r}. Use seconds, minutes, hours or days.")
    time.sleep(value * _UNITS[unit])
    
# --------------------------------------------------------------------------

def ai_detector(text: str) -> bool: #100% accuracy btw
    return "—" in text
