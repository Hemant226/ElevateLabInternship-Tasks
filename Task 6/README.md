# Task 6: Password Strength Analysis

## 🚀 Objective

This project was undertaken as part of a cyber security internship task. The primary goal was to gain a practical understanding of what constitutes a strong password and to learn how to evaluate password strength effectively. This involved creating various passwords, testing them using online tools, researching common password attack vectors, and summarizing best practices for password security.

## 🛠️ How I Approached This Task

1.  **Password Creation:** I started by creating a diverse set of passwords, ranging from very weak and common examples to much stronger, complex ones, including a passphrase. The idea was to test different lengths and combinations of characters (uppercase, lowercase, numbers, symbols).

2.  **Strength Evaluation:** Each password was then tested using an online password strength checker (`passwordmeter.com`) to get an objective measure of its strength and to understand the factors contributing to the score.

3.  **Research:** I researched common password attack methods, specifically focusing on:
    * Brute Force Attacks
    * Dictionary Attacks

4.  **Analysis & Reporting:** The results from the password tests and the research were compiled to identify best practices for creating strong passwords and to understand how password complexity directly impacts security.

## 🔧 Tools Used

* **Password Strength Checker:** [passwordmeter.com](https://www.passwordmeter.com/)

## 📊 Summary of Password Test Results

I tested several passwords, and here's a quick overview of what I found. The scores are from `passwordmeter.com`:

| Password Tested              | Score (from passwordmeter.com) | Complexity    | Key Observations                                                                       |
| :--------------------------- | :----------------------------- | :------------ | :------------------------------------------------------------------------------------- |
| `123456`                     | 4%                             | Very Weak     | Extremely common, short, numbers only. [cite: 2]                                           |
| `qwerty`                     | 8%                             | Very Weak     | Common keyboard pattern, short, predictable. [cite: 2]                                      |
| `thisisalongpassword`        | 20%                            | Weak          | Long, but only lowercase letters; no numbers or symbols. [cite: 2]                           |
| `MyNewPassword`              | 50%                            | Good          | Mix of uppercase and lowercase, but missing numbers/symbols. [cite: 2]                   |
| `MyNewPassword123`           | 100%                           | Very Strong   | Good length, includes uppercase, lowercase, and numbers. [cite: 2]                          |
| `MyN@wP&ssw0rd!2025`         | 100%                           | Very Strong   | Excellent mix of uppercase, lowercase, numbers, and symbols; good length. [cite: 2]       |
| `IloveEatingMangoesInSummer!`| 100%                           | Very Strong   | Long passphrase, good complexity with mixed case and a symbol. [cite: 2]                  |

*For detailed scoring criteria breakdown, please refer to the screenshots of passwordmeter.com results for each password (provided separately or in the full project report).*

## 💡 Key Learnings & Best Practices

Based on the tests and research, here are the main takeaways for creating strong passwords:

* **Length is Crucial:** Aim for at least 12-15 characters, if not more. Longer passwords are significantly harder to crack. [cite: 3]
* **Mix It Up:** Combine uppercase letters, lowercase letters, numbers, and symbols. [cite: 5] This drastically increases the complexity.
* **Avoid the Obvious:** Steer clear of dictionary words, common patterns (like `qwerty`), and easily guessable personal information (birthdays, names). [cite: 6]
* **Unpredictability Matters:** Randomness makes a password much stronger. `MyN@wP&ssw0rd!2025` is far better than a simpler variation. [cite: 7]
* **Consider Passphrases:** Memorable sentences or combinations of unrelated words can be both strong and easier to recall (e.g., `YellowTiger@Sky2024!`). [cite: 7]
* **Don't Reuse Passwords:** A compromised password shouldn't give access to multiple accounts. [cite: 3]
* **Use Password Managers:** These tools can generate and securely store very strong, unique passwords for all your accounts. [cite: 8]

## 🛡️ Understanding Password Attacks

A key part of this task was understanding *why* strong passwords are necessary.

### Brute Force Attacks
These attacks involve trying every possible combination of characters until the correct password is found. [cite: 9] The longer and more complex a password (more character types), the exponentially harder it is for a brute force attack to succeed. [cite: 12] Even a few extra characters or the addition of symbols can increase the time needed to crack a password from seconds to years.

### Dictionary Attacks
These attacks use predefined lists of common words, phrases, and known breached passwords to try and guess the correct one. [cite: 14, 15, 16] This is why using simple words like "password" or "sunshine" is very risky. [cite: 20] Complex, unique passwords not found in these dictionaries are the best defense. [cite: 24]

## ✅ Conclusion

This task provided valuable hands-on experience in password security. It's clear that creating strong, unique passwords (or passphrases) by combining length, mixed character types, and unpredictability is fundamental to protecting online accounts. Understanding the mechanics of common attacks like brute force and dictionary attacks further emphasizes the importance of these practices. Using tools like password strength checkers and password managers can also significantly enhance personal cyber security.
