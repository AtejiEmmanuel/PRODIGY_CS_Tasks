# Password Complexity Checker Task

A Python-based command-line tool that evaluates password strength against multiple security criteria and provides actionable feedback.

## Task Overview

This tool analyzes passwords based on security best practices and helps users create stronger passwords by offering specific improvement suggestions.

## Development Process

### 1. Initial Setup
```bash
mkdir password_checker
cd password_checker
touch password_checker.py
chmod +x password_checker.py
```

### 2. Core Password Checker Implementation

Built the initial version with basic security checks:
- Password length (8+ characters minimum, 12+ recommended)
- Character type verification (uppercase, lowercase, numbers, special characters)
- Common password pattern detection

### 3. Security Enhancement

Added advanced security features:
- Repetitive character detection (e.g., "aaa", "111")
- Sequential character detection (e.g., "abc", "123")
- Keyboard pattern detection (e.g., "qwerty")
- Character diversity analysis
- Expanded common weak password database

### 4. User Interface Design

Implemented user-friendly features:
- Masked password input for privacy
- Color-coded visual strength indicator
- Detailed feedback with specific improvement suggestions
- Clean command-line interface

## How to Run

1. Ensure Python 3 is installed
2. Navigate to the project directory
3. Run: `python3 password_checker.py`
4. Follow the on-screen prompts

## Scoring System

Passwords are evaluated on a point system and classified as:
- **Weak** (≤2 points): Significant security issues
- **Moderate** (3-4 points): Reasonable but improvable security
- **Strong** (5-6 points): Good security measures
- **Very Strong** (7+ points): Excellent security characteristics

## Demo
![Image Alt](https://github.com/AtejiEmmanuel/PRODIGY_CS_Tasks/blob/main/PRODIGY_CS_02/Task%202.png?raw=true)

![Image Alt](https://github.com/AtejiEmmanuel/PRODIGY_CS_Tasks/blob/main/PRODIGY_CS_02/Task%202a.png?raw=true)

