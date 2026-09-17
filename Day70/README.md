
# Day 70 — Blog Capstone Project Part 5: Deploying Your Web Application

## 🚀 Blog Capstone Project — Deployment

Day 70 focuses on taking the Flask Blog application developed in the previous days and **deploying it so that it can be accessed online**.

The project now moves from running only on a local computer to being hosted on a production server.

---

## [Phillip's Blog](https://phillip-blog.herokuapp.com/)
![day70](full_blog.gif)

## 📌 What I Learned

* How web applications are deployed
* Difference between development and production environments
* Using environment variables
* Preparing a Flask application for deployment
* Using a production WSGI server
* Deploying a Flask application to a hosting platform
* Managing dependencies with `requirements.txt`
* Using Git/GitHub for deployment
* Understanding production configuration
* Debugging deployment issues

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Login**
* **SQLite**
* **HTML/CSS**
* **Bootstrap**
* **Jinja2**
* **Git & GitHub**
* **WSGI**
* **Cloud Hosting**

---

## 🌐 Local vs Production

During development, the application runs locally:

```text
My Computer
     ↓
Flask Development Server
     ↓
localhost
```

After deployment:

```text
User's Browser
      ↓
Internet
      ↓
Cloud Server
      ↓
Flask Application
      ↓
Database
```

The main goal is to make the application accessible through a public URL.

---

## 🔧 Development Server vs Production Server

Flask's built-in development server is useful while building and testing the application.

Example:

```bash
flask run
```

or:

```bash
python main.py
```

However, the development server is **not intended for production use**.

A production deployment uses a proper WSGI server.

---

## 🧠 What is WSGI?

WSGI stands for:

**Web Server Gateway Interface**

It provides a standard way for a web server to communicate with a Python web application.

The simplified architecture is:

```text
Browser
   ↓
Web Server
   ↓
WSGI Server
   ↓
Flask Application
   ↓
Routes
   ↓
Database
```

A common production WSGI server for Python applications is:

```text
Gunicorn
```

---

## 📦 `requirements.txt`

A deployment platform needs to know which Python packages the project requires.

These dependencies are stored in:

```text
requirements.txt
```

Example:

```text
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
```

The server can then install the required packages.

---

## 🔐 Environment Variables

Sensitive information should not be hard-coded directly into the source code.

Examples include:

```text
SECRET_KEY
DATABASE_URL
API_KEY
PASSWORD
```

Instead of:

```python
SECRET_KEY = "my-secret-key"
```

we can use an environment variable:

```python
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
```

The actual value is stored in the hosting platform's environment/configuration settings.

---

## 🔑 Why Environment Variables Matter

Suppose the code contains:

```python
API_KEY = "123456789"
```

If the project is uploaded to GitHub, the key may become publicly visible.

A safer approach is:

```text
Environment Variable
        ↓
Hosting Platform
        ↓
Application
```

This keeps sensitive configuration outside the source code.

---

## 🗃️ Database Considerations

The blog uses a database to store information such as:

```text
Users
Blog Posts
Passwords/Password Hashes
```

Locally, the application may use:

```text
SQLite
```

However, deployment introduces an important issue:

> A local SQLite database file is not automatically the same thing as a reliable production database.

Production applications often use a hosted relational database such as PostgreSQL.

---

## 📁 Project Structure

A typical project structure can look like:

```text
blog-project/
│
├── static/
│   ├── css/
│   └── img/
│
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── login.html
│   ├── register.html
│   ├── make-post.html
│   ├── about.html
│   └── contact.html
│
├── main.py
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
```

---

## 📄 `.gitignore`

Some files should not be uploaded to GitHub.

Examples:

```text
.venv/
__pycache__/
.env
*.pyc
instance/
```

The `.gitignore` file tells Git which files to ignore.

---

## 📝 Procfile

Some deployment platforms use a `Procfile` to determine how the application should start.

A typical Flask deployment command might look like:

```text
web: gunicorn main:app
```

Here:

```text
main
```

refers to the Python file:

```text
main.py
```

and:

```text
app
```

refers to the Flask application object:

```python
app = Flask(__name__)
```

So:

```text
main:app
```

means:

```text
main.py → app
```

---

## 🔄 Git and Deployment

The general workflow is:

```text
Build Application
       ↓
Test Locally
       ↓
Create requirements.txt
       ↓
Create Git Repository
       ↓
Push to GitHub
       ↓
Connect Repository to Hosting Platform
       ↓
Configure Environment Variables
       ↓
Build Application
       ↓
Start Production Server
       ↓
Public URL
```

---

## 🧪 Testing Before Deployment

Before deploying, make sure:

* Registration works
* Login works
* Logout works
* Password hashing works
* Blog posts load correctly
* Protected routes work
* Database operations work
* Static files load
* Templates render correctly
* No secret keys are committed
* `requirements.txt` contains required packages

---

## 🐛 Common Deployment Problems

### 1. Module not found

```text
ModuleNotFoundError
```

Usually means a required package isn't installed.

Check:

```text
requirements.txt
```

---

### 2. Application doesn't start

Check the start command:

```text
gunicorn main:app
```

Make sure the filename and Flask app variable are correct.

---

### 3. Environment variable missing

If your application expects:

```python
os.environ.get("SECRET_KEY")
```

make sure `SECRET_KEY` is configured on the hosting platform.

---

### 4. Database problems

A local:

```text
SQLite database
```

may not behave the same way in a deployed environment.

Production applications generally need a persistent database service.

---

## 🧠 Key Concepts

### Development

```text
Developer
   ↓
Code
   ↓
Flask Development Server
   ↓
localhost
```

### Production

```text
User
 ↓
Internet
 ↓
Hosting Platform
 ↓
Production Server
 ↓
WSGI
 ↓
Flask
 ↓
Database
```

---

## 🎯 Skills Practiced

* Flask deployment
* Production configuration
* WSGI
* Gunicorn
* Git/GitHub
* Environment variables
* Dependency management
* `.gitignore`
* Database deployment considerations
* Debugging production applications

---

## 💡 Key Takeaways

1. Flask's development server is mainly for development and testing.
2. Production applications should use an appropriate WSGI server.
3. `requirements.txt` defines the Python dependencies.
4. Secrets should be stored using environment variables rather than hard-coded.
5. `.gitignore` prevents unnecessary or sensitive files from being committed.
6. Deployment connects your application to the internet.
7. A production database needs to be considered separately from a local SQLite file.
8. Git/GitHub makes it easier to version and deploy applications.

---

## 🏁 Final Project

By the end of Day 70, the Blog Capstone Project has progressed from a simple local Flask application into a **deployed web application**.

The overall progression is:

```text
Flask Basics
     ↓
Blog Application
     ↓
Database
     ↓
Authentication
     ↓
Users
     ↓
Relationships
     ↓
Deployment
     ↓
🌐 Live Web Application
```

---

## 📚 Day 70 Summary

**Day:** 70
**Project:** Blog Capstone Project — Part 5
**Main Topic:** Deployment
**Framework:** Flask
**Database:** SQLite / Production Database Concepts
**Server:** WSGI / Gunicorn
**Version Control:** Git + GitHub

### Main Goal

> Take the Flask Blog application from local development and prepare/deploy it as a production web application.
