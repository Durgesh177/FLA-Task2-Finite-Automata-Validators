"""DFA that accepts exactly four decimal digits."""

DIGITS = set("0123456789")


def validate_pin(pin: str) -> bool:
    """Return True iff pin contains exactly four ASCII decimal digits.

    DFA states q0..q4 count digits consumed. q4 is accepting.
    Any non-digit or any symbol after q4 moves to q_dead.
    """
    state = "q0"
    transitions = {
        "q0": "q1",
        "q1": "q2",
        "q2": "q3",
        "q3": "q4",
    }

    for symbol in pin:
        if state == "q_dead":
            return False
        if symbol not in DIGITS:
            state = "q_dead"
        elif state in transitions:
            state = transitions[state]
        else:  # An extra character after the fourth digit.
            state = "q_dead"

    return state == "q4"


if __name__ == "__main__":
    examples = ["1234", "0000", "2580", "123", "12345", "12A4"]
    for value in examples:
        print(f"{value!r}: {'ACCEPT' if validate_pin(value) else 'REJECT'}")
