"""Product DFA for a simple password-format policy."""

UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER = set("abcdefghijklmnopqrstuvwxyz")
DIGITS = set("0123456789")
SPECIAL = set("@#$%&*")
MAX_LENGTH = 16
MIN_LENGTH = 8


def _class_of(char: str):
    if char in UPPER:
        return "upper"
    if char in LOWER:
        return "lower"
    if char in DIGITS:
        return "digit"
    if char in SPECIAL:
        return "special"
    return None


def validate_password(password: str) -> bool:
    """Return True iff the password satisfies the DFA policy.

    DFA state: (length, upper_seen, lower_seen, digit_seen, special_seen).
    The trap state is represented by None. Only the specified ASCII
    character classes are accepted; whitespace and other symbols are invalid.
    """
    state = (0, False, False, False, False)

    for char in password:
        if state is None:
            return False

        length, upper_seen, lower_seen, digit_seen, special_seen = state
        char_class = _class_of(char)

        if char_class is None or length == MAX_LENGTH:
            state = None  # q_dead
            continue

        upper_seen |= char_class == "upper"
        lower_seen |= char_class == "lower"
        digit_seen |= char_class == "digit"
        special_seen |= char_class == "special"

        state = (
            length + 1,
            upper_seen,
            lower_seen,
            digit_seen,
            special_seen,
        )

    if state is None:
        return False

    length, upper_seen, lower_seen, digit_seen, special_seen = state
    return (
        MIN_LENGTH <= length <= MAX_LENGTH
        and upper_seen
        and lower_seen
        and digit_seen
        and special_seen
    )


if __name__ == "__main__":
    examples = [
        "Abcdef1@", "Hello123#", "A1bcdef$", "XyZ9876&",
        "Ab1@", "abcdefgh1@", "ABCDEFGH1@", "Abcdefgh@", "Abcdefg1",
    ]
    for value in examples:
        print(f"{value!r}: {'ACCEPT' if validate_password(value) else 'REJECT'}")
