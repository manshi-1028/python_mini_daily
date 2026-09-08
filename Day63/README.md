# Day 63 - Virtual Bookshelf

A Flask web application that creates a virtual bookshelf using a database to store and manage books.

## Virtual Bookshelf
![day63](https://user-images.githubusercontent.com/98851253/162035331-cefbd488-261c-4897-9bbd-0ece40617ebb.gif)

## What This Project Does

The application:

1. Displays books stored in a database.
2. Allows users to add new books.
3. Allows users to edit book information.
4. Allows users to delete books.
5. Uses SQLite as the database.
6. Uses SQLAlchemy to interact with the database.
7. Uses Flask to create the web application.

## Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- Flask-SQLAlchemy
- HTML
- CSS
- Jinja

## Project Structure

```text
Day-63/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/
│   └── css/
│       └── styles.css
├── books.db
├── README.md
└── requirements.txt
