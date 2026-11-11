"""DFA for a deliberately simplified email-address subset.

Accepted form: alphanumeric-local@alphanumeric-domain.TLD
where TLD has at least two ASCII letters.
"""

import string

LETTERS = set(string.ascii_letters)
ALNUM = LETTERS | set(string.digits)


def validate_email(address: str) -> bool:
    """Return True iff address matches [A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}.

    States:
      q0: start
      q1: reading local part
      q2: reading domain label
      q3: dot read; waiting for first TLD letter
      q4: at least two TLD letters read (accepting)
      q_dead: invalid input
    """
    state = "q0"

    for char in address:
        if state == "q0":
            state = "q1" if char in ALNUM else "q_dead"
        elif state == "q1":
            if char in ALNUM:
                state = "q1"
            elif char == "@":
                state = "q2"
            else:
                state = "q_dead"
        elif state == "q2":
            if char in ALNUM:
                state = "q2"
            elif char == ".":
                state = "q3"
            else:
                state = "q_dead"
        elif state == "q3":
            state = "q4" if char in LETTERS else "q_dead"
        elif state == "q4":
            state = "q4" if char in LETTERS else "q_dead"
        else:
            state = "q_dead"

        if state == "q_dead":
            return False

    return state == "q4"


if __name__ == "__main__":
    examples = [
        "ben@gmail.com", "user1@site.in", "abc123@domain.org",
        "A9@X2.co", "student2026@univ.edu", "@gmail.com",
        "usergmail.com", "user@.com", "user@domain.c", "user@domain.c0m",
    ]
    for value in examples:
        print(f"{value!r}: {'ACCEPT' if validate_email(value) else 'REJECT'}")
