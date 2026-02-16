# Day 1 Dictionary Mad Libs (NO nested dictionaries)
# -------------------------------------------------
# You are GIVEN: TEMPLATE, PROMPTS, RULES, state
# You must COMPLETE the TODO functions:
#   1) validate_input
#   2) collect_answers
#   3) score_answers
#   4) play_once

TEMPLATE = (
    "I was waiting for the {adj1} train at {num1} o’clock when a {noun1} "
    "{verb_past1} past me and shouted, “{exclaim1}!” "
    "I grabbed my {noun2} and ran {num2} steps to the {noun3}."
)

# PROMPTS is a dictionary:
#   key   = placeholder name (must match TEMPLATE placeholders)
#   value = what we ask the user to type
PROMPTS = {
    "adj1": "Enter an adjective:",
    "num1": "Enter a number (0-23):",
    "noun1": "Enter a noun:",
    "verb_past1": "Enter a past-tense verb:",
    "exclaim1": "Enter an exclamation (one word):",
    "noun2": "Enter a noun:",
    "num2": "Enter a number (1-500):",
    "noun3": "Enter a noun:",
}

# RULES is a dictionary:
#   key   = placeholder name (only for some placeholders)
#   value = a rule dictionary describing how to validate the input
#  we access a dictionary within a dictionary like it is a nested loop
#  For instance, to access num1's max value 23 : RULES["num1"]["max"]
#  To access the value word of exclaim1 : RULES["exclaim1"]["type"]

RULES = {
    "num1": {"type": "int", "min": 0, "max": 23},
    "num2": {"type": "int", "min": 1, "max": 500},
    "exclaim1": {"type": "word"},
}

# state tracks information across multiple plays
state = {
    "plays_total": 0,
    "best_score": None,
}


def validate_input(key, raw, rules):
    """
    Validate ONE user entry.

    Parameters:
      key   : the placeholder key (example: "num1" or "noun2")
      raw   : the user's raw input (a string)
      rules : the RULES dictionary

    Return:
      (ok, value, error_message)
        ok = True/False
        value = cleaned value (string or int) if ok is True, else None
        error_message = "" if ok is True, else a message to show the user

    Rules supported:
      - If key NOT in rules: accept any non-empty string (strip whitespace)
      - {"type":"int", "min":..., "max":...}
      - {"type":"word"}  -> one word only (no spaces), not empty

    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    # TODO 1: get the rule for this key using rules.get(key)
    rule = rules.get(key)
    stripped = raw.strip()

    # TODO 2: if there is NO rule, return (True, stripped_input, "")
    if rule is None:
        if stripped == "":
            return False, None, "Invalid input, please enter a value"
        else:
            return True, stripped, ""

    # TODO 3: if type == "int":
    #         - try to convert stripped_input to int
    #         - if it fails, return (False, None, "Please enter a valid integer.")
    #         - enforce min/max if present
    if rule["type"] == "int":
        try:
            stripped = int(stripped)
        except ValueError as v:
            return False, None, "Please enter a valid integer."

        if "min" in rule:
            if stripped < rule["min"]:
                return False, None, f"Value must be greater than {rule['min']}"

        if "max" in rule:
            if stripped > rule["max"]:
                return False, None, f"Value must be less than {rule['max']}"

        return True, stripped, ""

    # TODO 4: if type == "word":
    #         - stripped input must be non-empty
    #         - must NOT contain spaces
    if rule["type"] == "word":
        if stripped == "" or " " in stripped:
            return False, None, "Word must not be empty and must not have any spaces"
        return True, stripped, ""

    # TODO 5: if unknown rule type, treat it like a normal string
    if stripped == "":
        return False, None, "Invalid input"

    return False, None, "TODO: implement validate_input"


def collect_answers(prompts, rules):
    """
    Build the answers dictionary.

    prompts: PROMPTS dict (placeholder -> prompt)
    rules  : RULES dict (placeholder -> rule)
    
    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"] 

    Returns:
      answers dict where:
        key   = placeholder name (example: "noun1")
        value = validated user input (string or int)

    Requirements:
      - Start with answers = {}
      - Loop through prompts.items()
      - For each key:
          keep prompting until validate_input(...) returns ok=True
      - Store answers using answers[key] = value
    """
    # TODO: implement collect_answers
    # Hint: you'll want a while True loop inside the for-loop
    answers = {}
    for key, value in prompts.items():
        while True:
            user_input = input(prompts[key])
            ok, item, message = validate_input(key, user_input, rules)
            if not ok:
                continue
            else:
                answers[key] = item
                break
    return answers






def score_answers(answers, rules):
    """
    Compute a score for one round.

    Recommended scoring:
      - +1 for each answer key in answers
      - +2 bonus if that key also appears in rules

    Example:
      If answers has 8 keys, and 3 keys are in rules:
        score = 8*1 + 3*2 = 14


    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    # TODO: implement score_answers
    # Requirements:
    #   - iterate over the dictionary keys in answers (for key in answers:)
    #   - use membership test (if key in rules:)
    score = 0
    for key in answers:
        score += 1
        if key in rules:
            score += 2


    return score


def play_once():
    """
    Play one round of Mad Libs.

    Steps:
      1) Collect answers into a dictionary
      2) Fill TEMPLATE using TEMPLATE.format_map(answers)
      3) Score the round
      4) Update state:
          - plays_total increases by 1
          - best_score updates if this score is higher
      5) Print:
          - completed story
          - answers dict
          - score
    """
    print("\nFill in the blanks (you won't see the full story until the end!)\n")

    # TODO 1: answers = collect_answers(PROMPTS, RULES)
    answers = collect_answers(PROMPTS, RULES)
    # TODO 2: finished = TEMPLATE.format_map(answers)
    finished = TEMPLATE.format_map(answers)
    # TODO 3: score = score_answers(answers, RULES)
    score = score_answers(answers, RULES)
    # TODO 4: update state["plays_total"] and state["best_score"]
    state["plays_total"] += 1
    if state["best_score"] is None or score > state["best_score"]:
        state["best_score"] = score
    # TODO 5: print the finished story + answers dict + score

    print(finished)
    print(answers)
    print(score)


def main():
    """

    What main  does:
    - Repeatedly asks the user if they want to play
    - Calls play_once() when the user says 'y'
    - Stops when the user says 'n'
    - Prints a summary using the state dictionary
    """

    print("Mad Libs ")

    # TODO (READ ONLY): This while loop keeps the program running
    # until the user chooses to stop.

    while True:
        # TODO (READ ONLY): Get user choice and normalize it
        user_choice = input("Would you like to play?(y/n)")
        # TODO (READ ONLY): Stop the game loop if user types 'n'
        if user_choice.lower() == "n":
            break

        # TODO (READ ONLY): Play one full round if user types 'y'
        if user_choice.lower() == "y":
            play_once()
        # TODO (READ ONLY): Any other input is invalid
        else:
            print("Invalid choice")
            continue

    # TODO (READ ONLY): After the loop ends, print summary info
    # using the state dictionary.
    print(state)



if __name__ == "__main__":
    main()
