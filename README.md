# Password Checker - "SecuroPass"

## Introduction
"SecuroPass" is a simple Python program designed to help users check the strength of their passwords. It ensures password confidentiality by not displaying the input characters during entry.

## Usage
To run the program, execute the `pass.py` script. Upon execution, the program prompts the user to input a password. The password input is kept secret, ensuring privacy. After the initial input, the user is prompted to re-enter the password. If the two inputs match, the program evaluates the strength of the password and provides feedback. If not, the user is prompted to re-enter both passwords until they match.

## Strength Evaluation
"SecuroPass" assesses the strength of the password based on the following criteria:
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of digits
- Presence of special characters
- Length of the password

Based on these criteria, the program categorizes the password strength as follows:
- Very weak
- Weak
- Decent
- Strong
- Very strong

## Extending the Project
This project can be extended by implementing features to generate random passwords. By adding functionality to generate strong passwords, users can enhance their online security further.
