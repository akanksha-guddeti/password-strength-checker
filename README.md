# 🔐 Password Strength Checker

A simple and user-friendly **Password Strength Checker** built with Python and Streamlit.

It checks whether a password follows important security requirements and gives a clear strength score.

## ✨ Features

- 🔤 Checks minimum 8 characters
- ⬆️ Checks for uppercase letters
- 🔡 Checks for lowercase letters
- 🔢 Checks for numbers
- ✨ Checks for special characters
- 📊 Displays password security score
- 💪 Shows password strength
- 🛡️ Displays individual security requirements
- 👁️ Password visibility option
- 💡 Provides quick password security tips
- 🎨 Clean and attractive Streamlit interface

## 🛡️ Security Requirements

A strong password should contain:

- ✅ At least 8 characters
- ✅ At least one uppercase letter
- ✅ At least one lowercase letter
- ✅ At least one number
- ✅ At least one special character

## 📊 Strength Levels

| Score | Strength |
|------|----------|
| 0–1 | 🔴 Very Weak |
| 2 | 🟠 Weak |
| 3 | 🟡 Medium |
| 4 | 🔵 Strong |
| 5 | 🟢 Very Strong |

## 🛠️ Technologies Used

- 🐍 Python
- 🎈 Streamlit
- 🔎 Regular Expressions (`re`)

## 📁 Project Structure

```text
password-strength-checker/
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/akanksha-guddeti/password-strength-checker.git
2. Open the project folder
cd password-strength-checker
3. Install the required packages
pip install -r requirements.txt
▶️ Run the Application

Run the following command:

streamlit run app.py

If streamlit command does not work, use:

python -m streamlit run app.py

The application will open in your browser.

💡 How It Works
Enter a password in the password field.
The application checks the password against five security rules.
Each requirement is marked as passed or required.
A security score is calculated.
The application displays the overall password strength.
Security tips are provided to help create stronger passwords.
🔒 Privacy

The Password Strength Checker is designed as a local application.

Passwords are checked within the application and are not intentionally stored by this project.

For real-world security applications, passwords should never be stored as plain text.

🎯 Project Goal

The goal of this project is to demonstrate basic password-security concepts and Python programming using an interactive web interface.

🚀 Future Improvements
Add password entropy calculation
Detect common passwords
Detect repeated characters
Add password generator
Add estimated crack-time information
Improve security analysis
👩‍💻 Author

Akanksha Guddeti

GitHub: https://github.com/akanksha-guddeti
