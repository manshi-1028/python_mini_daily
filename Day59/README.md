# Day 59 - Blog Capstone Part 2

A multi-page blog website built using Flask, Jinja, Bootstrap, and an external API.

## Blog Capstone Project Part 2 - Adding Styling
![day59](blog.gif)

## What This Project Does

The website:

1. Uses Flask to create multiple pages.
2. Uses Bootstrap for responsive styling.
3. Uses Jinja templates for reusable HTML.
4. Uses `include` to reuse common components.
5. Fetches blog posts from an API.
6. Dynamically displays individual blog posts.
7. Includes Home, About, Contact, and Blog Post pages.

## Technologies Used

* Python
* Flask
* Jinja
* Bootstrap
* HTML
* CSS
* REST API
* Requests

## Project Structure

```text
Day-59-Blog/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── post.html
│   ├── header.html
│   └── footer.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── assets/
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install flask requests
```

Or:

```bash
pip install -r requirements.txt
```

## How It Works

The Flask application creates different routes for different pages.

Blog posts are retrieved from an external API and passed to Jinja templates.

Example:

```python
posts = requests.get(API_URL).json()
return render_template("index.html", posts=posts)
```

Jinja then displays the posts dynamically.

## Jinja Include

Common elements such as the header and footer can be reused:

```html
{% include "header.html" %}
```

and:

```html
{% include "footer.html" %}
```

This avoids repeating the same HTML on every page.

## Dynamic Blog Posts

A blog post can be opened using a dynamic URL:

```text
/post/1
```

The post ID is used to display the correct blog post.

## Bootstrap

Bootstrap is used to create:

* Responsive layouts
* Navigation bars
* Buttons
* Cards
* Typography
* Mobile-friendly pages

## Concepts Practiced

* Flask routing
* Jinja templating
* `{% include %}`
* `{% extends %}`
* `{% block %}`
* Bootstrap
* Responsive design
* API requests
* JSON data
* Dynamic URLs
* `render_template()`
* Passing data from Python to HTML



## Running the Project

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Learning Outcome

Day 59 combines Flask, Jinja, Bootstrap, APIs, and template reuse to build a complete multi-page dynamic blog website.

## Disclaimer

This project was created for educational purposes as part of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.


