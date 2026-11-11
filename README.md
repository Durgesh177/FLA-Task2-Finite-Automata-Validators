# FLA Task 2 – Finite Automata Validators

**Course:** 21CSC301T – Formal Language and Automata  
**Student:** Bennu Durgesh Naraharisetti  
**Register Number:** RA2411026050065

This repository contains Python implementations of three deterministic finite automata (DFAs) for real-time input-format validation.

## Applications

1. **ATM PIN validator** – accepts exactly four decimal digits.
2. **Password policy validator** – accepts 8–16 permitted characters with at least one uppercase letter, lowercase letter, digit, and special character from `@ # $ % & *`.
3. **Email format validator** – accepts the educational subset `alphanumeric-local@alphanumeric-domain.TLD`, where the TLD contains at least two English letters.

> These are format validators for an automata assignment. They do not authenticate users, verify stored PINs, confirm mailbox ownership, or provide production-grade password security.

## Repository structure

```text
FLA-Task2-Finite-Automata-Validators/
├── README.md
├── atm_pin_validator.py
├── password_validator.py
├── email_validator.py
└── test_cases.py
```

## Requirements

- Python 3.9 or later
- No third-party packages (standard library only)

## Run the validators

Run an individual program:

```bash
python atm_pin_validator.py
python password_validator.py
python email_validator.py
```

Run all automated test cases:

```bash
python -m unittest -v
```

## DFA models

### 1. ATM PIN

Let `D = {0,1,...,9}`. The language is:

```
L_PIN = { w in D* | length(w) = 4 }
```

The states `q0, q1, q2, q3, q4` record how many digits have been read. `q0` is the initial state, `q4` is the only accepting state, and `q_dead` is the trap state. Any non-digit or fifth character causes rejection.

### 2. Password policy

The permitted character classes are:

- `U`: uppercase English letter
- `L`: lowercase English letter
- `D`: decimal digit
- `S`: one of `@ # $ % & *`

A DFA state is represented by `(length, seen_upper, seen_lower, seen_digit, seen_special)`. The length counter is bounded at 16. Any disallowed character or character beyond the maximum length enters the trap state. A string is accepted at end-of-input only when its length is 8–16 and all four flags are true.

### 3. Email subset

The accepted pattern is:

```
[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}
```

The finite states track the local part, domain label, first TLD character, and at least two TLD characters. This intentionally restricted subset does not represent every address allowed by Internet email standards.

## Sample test results

The unit tests include at least five accepted and five rejected examples for each application. Execute `python -m unittest -v` to see the results.

## Academic note

A DFA is appropriate here because each validator needs only finite memory: a bounded character count, a finite set of flags, or a finite sequence of format stages. Semantic checks and external verification belong to the surrounding application, not to these automata.
