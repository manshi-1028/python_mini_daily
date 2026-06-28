# 🎂 Birthday Wisher

A Python automation project that sends personalized birthday wishes via email.

## Features

- Reads birthdays from a CSV file.
- Checks if today matches anyone's birthday.
- Randomly selects one of three birthday letter templates.
- Replaces the placeholder `[NAME]` with the recipient's name.
- Sends the birthday email automatically using SMTP.

## Project Structure

```
birthday-wisher/
│── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
│── birthdays.csv
│── main.py
│── README.md
│── requirements.txt
│── .gitignore
```

## CSV Format

```csv
name,email,year,month,day
John,john@example.com,1999,6,28
Jane,jane@example.com,2001,12,15
```

## Requirements

- Python 3.10+
- Gmail App Password (if using Gmail)

## Installation

Clone the repository.

```bash
git clone https://github.com/manshi-1028/birthday-wisher.git
```

Go into the project.

```bash
cd birthday-wisher
```

Run the program.

```bash
python main.py
```

## Letter Templates

The project randomly selects one of the templates from:

```
letter_templates/
```

and replaces:

```
[NAME]
```

with the recipient's actual name.

## Technologies Used

- Python
- csv
- smtplib
- datetime
- random

## Notes

For security reasons, do **not** commit your real email credentials to GitHub. Use environment variables or a `.env` file that is excluded by `.gitignore`.
